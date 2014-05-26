import pygtk
pygtk.require('2.0')
import gtk
import nltk

import socket
import sys

import subprocess

word_id1 = 0
word_id2 = 0
score1 = 0
score2 = 0
table = [[""]*5 for i in range(5)]
table[2][0] = "m"
table[2][1] = "a"
table[2][2] = "n"
table[2][3] = "g"
table[2][4] = "o"

# class word and count of letters in the word
class Word_cnt(object):
  def __init__(self, word=None,  cnt_letter=0):
    self.word = word
    self.cnt_letter = cnt_letter


class MyProgram:

  def __init__(self):
  # create a new window
  
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    app_window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    app_window.set_position(gtk.WIN_POS_CENTER)
    app_window.set_size_request(600, 500)
    app_window.set_border_width(10)
    app_window.set_title("BALDA")
    app_window.connect("delete_event", lambda w,e: gtk.main_quit())

    vbox_app = gtk.VBox(False, 0)
    app_window.add(vbox_app)
    vbox_app.show()

    table_big = gtk.Table(12, 3, True)	
    vbox_app.add(table_big)
    table_big.show()

    player_name_1 = gtk.Label("I")
    player_name_1.set_alignment(xalign=0.05, yalign=1)
    player_name_1.show()
    table_big.attach(player_name_1,0,1,0,1,0,0,0,0)	

    player_name_2 = gtk.Label("Opponent")
    player_name_2.set_alignment(xalign=0.05, yalign=1)
    player_name_2.show()
    table_big.attach(player_name_2,2,3,0,1,0,0,0,0)

    # main table 5 x 5 

    table_main = gtk.Table(rows=5, columns=5, homogeneous=True)

    letters = [[0]*5 for i in range(5)]

    for i in range(5):
      for j in range(5):
        letters[i][j] = gtk.Entry(1)
        letters[i][j].set_text("")
        letters[i][j].select_region(0, len(letters[i][j].get_text()))
        letters[i][j].set_width_chars(2)
        letters[i][j].show()
        table_main.attach(letters[i][j], j, j + 1, i, i + 1, 0,0,0,0)
    letters[2][0].set_text("m")
    letters[2][1].set_text("a")
    letters[2][2].set_text("n")
    letters[2][3].set_text("g")
    letters[2][4].set_text("o")	
    # table for first player
    table_layout_1 = gtk.Table(10, 2, False)
    player_1 = []
    player_table_1 = [[0]*10 for i in range(10)]	
    sum_1 = 0
    for i in range(10):
      player_1.append(Word_cnt('', 0))
      player_table_1[i][0] = gtk.Entry(15)
      player_table_1[i][0].set_text(player_1[i].word)
      player_table_1[i][0].set_width_chars(15)
      player_table_1[i][0].show()
      table_layout_1.attach(player_table_1[i][0], 0, 1, i, i + 1, 0,0,0,0)
      player_table_1[i][1] = gtk.Entry(2)
      player_table_1[i][1].set_text(str(player_1[i].cnt_letter))
      player_table_1[i][1].set_width_chars(2)
      sum_1 = sum_1 + int(player_table_1[i][1].get_text())
      player_table_1[i][1].show()
      table_layout_1.attach(player_table_1[i][1], 1, 2, i, i + 1, 0,0,0,0)
    table_layout_1.set_col_spacing(0,4)

    # table for second player
    table_layout_2 = gtk.Table(10, 2, False)
    player_2 = []
    player_table_2 = [[0]*10 for i in range(10)]
    sum_2 = 0

    for i in range(10):
      player_2.append(Word_cnt('', 0))
      player_table_2[i][0] = gtk.Entry(15)
      player_table_2[i][0].set_text(player_2[i].word)
      player_table_2[i][0].set_width_chars(15)
      player_table_2[i][0].show()
      table_layout_2.attach(player_table_2[i][0], 0, 1, i, i + 1, 0,0,0,0)
      player_table_2[i][1] = gtk.Entry(2)
      player_table_2[i][1].set_text(str(player_2[i].cnt_letter))
      player_table_2[i][1].set_width_chars(2)
      player_table_2[i][1].show()
      sum_2 = sum_2 + player_2[i].cnt_letter
      table_layout_2.attach(player_table_2[i][1], 1, 2, i, i + 1, 0,0,0,0)
    table_layout_2.set_col_spacing(0,4)

    table_layout_1.show()
    table_main.show()
    table_layout_2.show()
    table_big.attach(table_layout_1,0,1,1,11,0,0,10,0)
    table_big.attach(table_main,1,2,3,8,0,0,10,0)
    table_big.attach(table_layout_2,2,3,1,11,0,0,15,0)

    #score
    scr_1 = gtk.Label("Score:")
    scr_1.set_alignment(xalign=0.05, yalign=1)
    scr_1.show()
    table_big.attach(scr_1,0,1,11,12,0,0,0,0)

    score_1 = gtk.Entry(2)
    score_1.set_text(str(sum_1))
    score_1.set_width_chars(2)
    score_1.show()
    table_big.attach(score_1,0,1,12,13,0,0,0,0)

    scr_2 = gtk.Label("Score:")
    scr_2.set_alignment(xalign=0.05, yalign=1)
    scr_2.show()
    table_big.attach(scr_2,2,3,11,12,0,0,0,0)

    score_2 = gtk.Entry(2)
    score_2.set_text(str(sum_2))
    score_2.set_width_chars(2)
    score_2.show()
    table_big.attach(score_2,2,3,12,13,0,0,0,0)	

    scrolled = gtk.ScrolledWindow()
    scrolled.set_border_width(5)
    scrolled.show()

    view = gtk.TextView()
    view.set_wrap_mode (gtk.WRAP_WORD)
    textbuffer = view.get_buffer()
    textbuffer.set_text('ololo')

    view.show()
    scrolled.add(view)	
    vbox_app.add(scrolled)
    

    btn_next = gtk.Button("NEXT")
    table_big.attach(btn_next,1,2,9,10,0,0,0,0)
    btn_next.connect("clicked", self.clicked_next, btn_next, s, player_table_1, player_table_2, letters, score_1, score_2, textbuffer)

    btn = gtk.Button("PLAY!")
    btn.set_sensitive(True)
    table_big.attach(btn,1,2,9,10,0,0,0,0)
    btn.connect("clicked", self.send_message, btn, btn_next, s, player_table_2, letters, score_1, score_2)
    btn.show()

    app_window.show()
      
      

  def clicked_next(self, widget, btn_next, s, player_table_1, player_table_2, letters, score_1, score_2,textbuffer):
    global word_id1
    global word_id2
    global table
    global score1
    global score2
    btn_next.set_sensitive(False)
    word1 = player_table_1[word_id1][0].get_text()
    score1 = score1 + len(word1)
    score_1.set_text(str(score1))
    player_table_1[word_id1][1].set_text(str(len(word1)))
    x = 0
    y = 0
    l = 0
    for i in range(5):
      for j in range(5):
        if (letters[i][j].get_text() != table[i][j]):
          x = i
          y = j
          l = letters[i][j].get_text()
          print(l)
    table[x][y] = l
    new_word1 = word1 + " " + str(x) + " " + str(y) + " " + l
    word_id1 = word_id1 + 1
    print(word_id1)
    s.send(new_word1)
    if (word_id1 == 2 and word_id2 == 2):
      print("finished")
      s.send(b"4")
      s.close()
      btn_next.set_sensitive(False)
      if (int(score_1.get_text()) >= int (score_2.get_text())):
        textbuffer.set_text("You win!")
      else:
        textbuffer.set_text("You loose :(")
      return
    new_word2 = s.recv(1024)
    if (len(new_word2) > 1):
      new_word2_list = nltk.word_tokenize(new_word2)
      player_table_2[word_id2][0].set_text(new_word2_list[0])
      player_table_2[word_id2][1].set_text(str(len(new_word2_list[0])))
      score2 = score2 + len(new_word2_list[0])
      score_2.set_text(str(score2))
      x_r = int(new_word2_list[1])
      y_r = int(new_word2_list[2])
      letters[x_r][y_r].set_text(new_word2_list[3])
      table[x_r][y_r] = new_word2_list[3]
      word_id2 = word_id2 + 1
      btn_next.set_sensitive(True)

    if (word_id1 == 2 and word_id2 == 2):
      print("finished")
      s.send(b"4")
      s.close()
      btn_next.set_sensitive(False)
      if (int(score_1.get_text()) >= int (score_2.get_text())):
        textbuffer.set_text("You win!")
      else:
        textbuffer.set_text("You loose :(")
      return

  def send_message(self, widget, btn, btn_next, s, player_table_2, letters, score_1, score_2):
    global word_id2
    global table
    global score1
    global score2
    s.connect(('127.0.0.1', 9100))
    s.send(b"1")
    btn.set_sensitive(False)
    data = s.recv(1024)
    if (data == b"1"):
      btn.destroy()
      btn_next.set_sensitive(True)
      s.send(b"2")
      btn_next.show()
    if (data == b"2"):
      btn.destroy()
      print("recieved", data)
      btn_next.set_sensitive(False)
      btn_next.show()
      new_word2 = s.recv(1024)
      if (len(new_word2) > 1):
        new_word2_list = nltk.word_tokenize(new_word2)
        player_table_2[word_id2][0].set_text(new_word2_list[0])
        player_table_2[word_id2][1].set_text(str(len(new_word2_list[0])))
        score2 = score2 + len(new_word2_list[0])
        score_2.set_text(str(score2))
        x_r = int(new_word2_list[1])
        y_r = int(new_word2_list[2])
        letters[x_r][y_r].set_text(new_word2_list[3])
        table[x_r][y_r] = new_word2_list[3]
        word_id2 = word_id2 + 1
        btn_next.set_sensitive(True)

def main():
  gtk.main()
  return 0

if __name__ == "__main__":
  MyProgram()
  main()

