import pandas as pd, random
from wordcloud import WordCloud

word_tag = pd.read_excel('兔年吉祥話.xlsx', engine = 'openpyxl', sheet_name = 0)


def word_cloud_generate(words, j):
    
    s = random.choice(range(4, 9))
    k = random.choices(list(range(words.shape[0])), k = s) 
    kws = ' '.join(words.iloc[k, 1].tolist())

    fonts = ['SourceHanSansTC/SourceHanSansTC-Regular.otf', 'SourceHanSansTC/SourceHanSansTC-ExtraLight.otf',
             'SourceHanSansTC/SourceHanSansTC-Heavy.otf', 'SourceHanSansTC/SourceHanSansTC-Medium.otf']
    
    def random_color_func(word = None, font_size = None, position = None, orientation = None, font_path = None, random_state = None):
        h = int(360.0 * float(random_state.randint(10, 250)) / 255.0)
        s = int(100.0 * float(random_state.randint(20, 200)) / 255.0)
        l = int(100.0 * float(random_state.randint(40, 140)) / 255.0)
        return "hsl({}, {}%, {}%)".format(h, s, l)

    mask_file = ['heart.png', 'crossroad_wt.png', 
                 'cycle.png', 'speak.png']
    
    mask_choice = [np.array(Image.open(mask_file[i])) for i in range(len(mask_file))]
    num_mask_choice = random.choices(range(len(mask_choice)))
    
    v = random.choice(range(len(fonts)))
    
    my_wordcloud = WordCloud(width = 100, height = 100, background_color = None, font_path = fonts[v], mask = mask_choice[num_mask_choice], max_words = 100, 
                             color_func = random_color_func, min_font_size = 12, mode = 'RGBA').generate(kws) 
        
    my_wordcloud.to_file('wordcloud/' + 'test_wordcolud_' + str(j) + '.png')
    return kws

test = [word_cloud_generate(word_tag, j) for j in range(41)]

########################################################################

from PIL import Image
from random import choice

word_path = ['wordcloud/' + 'test_wordcolud_' + str(j) + '.png' for j in range(41)]
back_color_path = ['temp1_back.png', 'temp2_back.png']
background_path = ['temp1.png', 'temp2.png']
space = [(750, 400), (550, 200)]
size = [(450, 450), (200, 200)]

def cover_word_pic(run, word_path, back_color_path, background_path, space, size):
    bc = choice(range(2))
    wc = choice(range(len(word_path)))
    
    word = Image.open(word_path[wc]).convert('RGBA').resize(size[bc])
    background = Image.open(back_color_path[bc]).convert('RGBA').resize(size[bc])
    
    combine0 = Image.new('RGBA', word.size)
    combine0 = Image.alpha_composite(combine0, background)
    combine0 = Image.alpha_composite(combine0, word)
    
    coverage0 = Image.open(background_path[bc]).convert('RGBA')
    coverage0.paste(combine0, space[bc])
    file = coverage0.save('words+pic_final/results_' + str(run) + '.png')
    return file

temp = [cover_word_pic(run, word_path, back_color_path, background_path, space, size) for run in range(10)]