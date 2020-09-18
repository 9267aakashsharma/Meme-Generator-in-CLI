#!/usr/bin/env python
# coding: utf-8

# In[7]:


from PIL import Image, ImageDraw, ImageFont
import textwrap
import argparse
import webbrowser


# In[8]:


def meme(location,top_text,bottom_text,Text_Color,Text_Size):
    im = Image.open(location)
    draw = ImageDraw.Draw(im)
    image_width, image_height = im.size
    font = ImageFont.truetype(font="./impact/impact.ttf", size=Text_Size)
    #top_text="sfsv"

    top_text = top_text.upper()
    bottom_text = bottom_text.upper()
    char_width, char_height = font.getsize('A')
    chars_per_line = image_width // char_width
    top_lines = textwrap.wrap(top_text, width=chars_per_line)
    bottom_lines = textwrap.wrap(bottom_text, width=chars_per_line)
    y = 10
    for line in top_lines:
        line_width, line_height = font.getsize(line)
        x = (image_width - line_width) / 2
        draw.text((x, y), line, fill=Text_Color, font=font)
        y += line_height
    y = image_height - char_height * len(bottom_lines) - 15
    for line in bottom_lines:
        line_width, line_height = font.getsize(line)
        x = (image_width - line_width) / 2
        draw.text((x, y), line, fill=Text_Color, font=font)
        y += line_height
    im.show()
    ask_save=input("Save the Image(Y/N) : ")
    ask_save=ask_save.upper()
    if (ask_save=='Y'):
        im.save('meme-' + im.filename.split('/')[-1])

    ask_post=input("Post to fb?(Y/N) : ")
    ask_post=ask_post.upper()
    if(ask_post=='Y'):
        webbrowser.open("http://fb.com", new=1)
# In[9]:

if __name__=='__main__':
    print("\n\n\n#        #  @@@@@@@ #        #  @@@@@@@        ")
    print("# #    # #  @       # #    # #  @              ")
    print("#  #  #  #  @       #  #  #  #  @                 ")
    print("#   #    #  @@@@    #   #    #  @@@@          ")
    print("#        #  @       #        #  @              ")
    print("#        #  @       #        #  @              ")
    print("#        #  @@@@@@@ #        #  @@@@@@@         \n\n\n ")

    parser =argparse.ArgumentParser(prog='Meme Generator',
                                    usage='''
                                    Usage:
                                    Upload the image and generate a meme !!!
                                    ''',
                                    description='''
                                    -----------------------------------------------
                                    Description:
                                    This tool will display generated meme .
                                    -----------------------------------------------
                                    ''',
                                    epilog="Copyrights @Garvit_Sharma",
                                    formatter_class=argparse.RawDescriptionHelpFormatter,
                                    add_help=True
                                    )




    location=input("Location of your Picture : ")
    top=input("Top Text : ")
    bottom=input("Bottom Text : ")
    Text_Color=input("Color of your Text : ")
    Text_Size=int(input("Size of Text(Greater than 20 would be a good choice) : "))
    meme(location,top,bottom,Text_Color,Text_Size)
# In[ ]:




