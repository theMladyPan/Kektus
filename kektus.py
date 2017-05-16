#Boa:Frame:Frame1

import wx, sys, time

def create(parent, verbose):
    return Frame1(parent, verbose)

[wxID_FRAME1, wxID_FRAME1BETON_CHOICE, wxID_FRAME1CHECKBOX1, 
 wxID_FRAME1KAMENIVO_CHOICE, wxID_FRAME1KRYCIA_VRSTVA_ENTRY, 
 wxID_FRAME1MIN_KRYTIE_ENTRY, wxID_FRAME1OCEL_CHOICE, 
 wxID_FRAME1PROSTREDIE_CHOICE, wxID_FRAME1PRUTY_LIST, 
 wxID_FRAME1STATICBITMAP1, wxID_FRAME1STATICBOX1, wxID_FRAME1STATICBOX2, 
 wxID_FRAME1STATICBOX3, wxID_FRAME1STATICBOX4, wxID_FRAME1STATICBOX5, 
 wxID_FRAME1STATICBOX6, wxID_FRAME1STATICBOX7, wxID_FRAME1STATICBOX8, 
 wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT10, wxID_FRAME1STATICTEXT11, 
 wxID_FRAME1STATICTEXT12, wxID_FRAME1STATICTEXT13, wxID_FRAME1STATICTEXT14, 
 wxID_FRAME1STATICTEXT15, wxID_FRAME1STATICTEXT16, wxID_FRAME1STATICTEXT17, 
 wxID_FRAME1STATICTEXT18, wxID_FRAME1STATICTEXT19, wxID_FRAME1STATICTEXT2, 
 wxID_FRAME1STATICTEXT20, wxID_FRAME1STATICTEXT21, wxID_FRAME1STATICTEXT22, 
 wxID_FRAME1STATICTEXT23, wxID_FRAME1STATICTEXT24, wxID_FRAME1STATICTEXT25, 
 wxID_FRAME1STATICTEXT26, wxID_FRAME1STATICTEXT27, wxID_FRAME1STATICTEXT28, 
 wxID_FRAME1STATICTEXT29, wxID_FRAME1STATICTEXT3, wxID_FRAME1STATICTEXT30, 
 wxID_FRAME1STATICTEXT31, wxID_FRAME1STATICTEXT32, wxID_FRAME1STATICTEXT33, 
 wxID_FRAME1STATICTEXT34, wxID_FRAME1STATICTEXT35, wxID_FRAME1STATICTEXT36, 
 wxID_FRAME1STATICTEXT37, wxID_FRAME1STATICTEXT38, wxID_FRAME1STATICTEXT39, 
 wxID_FRAME1STATICTEXT4, wxID_FRAME1STATICTEXT40, wxID_FRAME1STATICTEXT41, 
 wxID_FRAME1STATICTEXT42, wxID_FRAME1STATICTEXT43, wxID_FRAME1STATICTEXT5, 
 wxID_FRAME1STATICTEXT6, wxID_FRAME1STATICTEXT7, wxID_FRAME1STATICTEXT8, 
 wxID_FRAME1STATICTEXT9, wxID_FRAME1STRMENE_CHOICE, wxID_FRAME1TEXTCTRL1, 
 wxID_FRAME1TEXTCTRL10, wxID_FRAME1TEXTCTRL11, wxID_FRAME1TEXTCTRL12, 
 wxID_FRAME1TEXTCTRL2, wxID_FRAME1TEXTCTRL3, wxID_FRAME1TEXTCTRL4, 
 wxID_FRAME1TEXTCTRL5, wxID_FRAME1TEXTCTRL6, wxID_FRAME1TEXTCTRL7, 
 wxID_FRAME1TEXTCTRL8, wxID_FRAME1TEXTCTRL9, wxID_FRAME1TOLERANCIA_SPIN, 
 wxID_FRAME1VYSTUZ_CHOICE, wxID_FRAME1VYSTUZ_PREF_CHOICE, 
] = [wx.NewId() for _init_ctrls in range(77)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(953, 0), size=wx.Size(974, 1047),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Kektus')
        self.SetClientSize(wx.Size(958, 1008))
        self.SetToolTipString(u'Kektus v\xfdpo\u010dtov\xfd program, \ncopyright Rubint bros. 2016')
        self.SetIcon(wx.Icon(u'kektus.ico',wx.BITMAP_TYPE_ICO))
        self.SetBackgroundColour(wx.Colour(120, 120, 120))

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.NullBitmap,
              id=wxID_FRAME1STATICBITMAP1, name='staticBitmap1', parent=self,
              pos=wx.Point(8, 24), size=wx.Size(288, 488), style=0)
        self.staticBitmap1.SetToolTipString(u'Prierez')
        self.staticBitmap1.SetHelpText(u'Prierez materi\xe1lu')
        self.staticBitmap1.SetCursor(wx.CROSS_CURSOR)

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME1STATICBOX1,
              label=u'Prierez nosn\xedka', name='staticBox1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(304, 520), style=0)

        self.staticBox2 = wx.StaticBox(id=wxID_FRAME1STATICBOX2,
              label=u'Materi\xe1ly', name='staticBox2', parent=self,
              pos=wx.Point(312, 0), size=wx.Size(304, 88), style=0)
        self.staticBox2.SetToolTipString(u'')

        self.beton_choice = wx.Choice(choices=["C20/25", "C25/30", "C30/37"],
              id=wxID_FRAME1BETON_CHOICE, name=u'beton_choice', parent=self,
              pos=wx.Point(472, 24), size=wx.Size(104, 23), style=0)
        self.beton_choice.SetToolTipString(u'Trieda bet\xf3nu')
        self.beton_choice.SetStringSelection(u'')
        self.beton_choice.SetLabelText(u'C20/25')
        self.beton_choice.SetSelection(0)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='staticText1', name='staticText1', parent=self,
              pos=wx.Point(320, 32), size=wx.Size(31, 16), style=0)
        self.staticText1.SetToolTipString(u'')
        self.staticText1.SetLabelText(u'Bet\xf3n')

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label='staticText2', name='staticText2', parent=self,
              pos=wx.Point(320, 56), size=wx.Size(26, 16), style=0)
        self.staticText2.SetLabelText(u'Oce\u013e')
        self.staticText2.SetToolTipString(u'')

        self.ocel_choice = wx.Choice(choices=["B400A", "B400B", "B500A",
              "B500B"], id=wxID_FRAME1OCEL_CHOICE, name=u'ocel_choice',
              parent=self, pos=wx.Point(472, 48), size=wx.Size(104, 23),
              style=0)
        self.ocel_choice.SetToolTipString(u'Typ beton\xe1rskej v\xfdstu\u017ee')
        self.ocel_choice.SetLabelText(u'B500B')
        self.ocel_choice.SetSelection(3)

        self.staticBox3 = wx.StaticBox(id=wxID_FRAME1STATICBOX3,
              label='staticBox3', name='staticBox3', parent=self,
              pos=wx.Point(312, 88), size=wx.Size(304, 88), style=0)
        self.staticBox3.SetToolTipString(u'Vn\xfatorn\xe9 sily')
        self.staticBox3.SetLabelText(u'Vn\xfatorn\xe9 sily')

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label='staticText3', name='staticText3', parent=self,
              pos=wx.Point(320, 120), size=wx.Size(100, 16), style=0)
        self.staticText3.SetLabelText(u'Ohybov\xfd moment:')
        self.staticText3.SetToolTipString(u'')

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self, pos=wx.Point(472, 112), size=wx.Size(104, 23),
              style=0, value='textCtrl1')
        self.textCtrl1.SetToolTipString(u'Ohybov\xfd moment v kN.m')
        self.textCtrl1.SetLabelText(u'37.3')
        self.textCtrl1.SetHint(u'')
        self.textCtrl1.SetHelpText(u'')

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
              label='staticText4', name='staticText4', parent=self,
              pos=wx.Point(584, 120), size=wx.Size(29, 16), style=0)
        self.staticText4.SetLabelText(u'kN.m')
        self.staticText4.SetToolTipString(u'')

        self.staticText5 = wx.StaticText(id=wxID_FRAME1STATICTEXT5,
              label='staticText5', name='staticText5', parent=self,
              pos=wx.Point(320, 144), size=wx.Size(62, 16), style=0)
        self.staticText5.SetHelpText(u'')
        self.staticText5.SetLabelText(u'Prie\u010dna sila:')
        self.staticText5.SetToolTipString(u'')

        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL2, name='textCtrl2',
              parent=self, pos=wx.Point(472, 136), size=wx.Size(104, 23),
              style=0, value='textCtrl2')
        self.textCtrl2.SetToolTipString(u'Prie\u010dna sila v kN')
        self.textCtrl2.SetLabelText(u'25.0')

        self.staticText6 = wx.StaticText(id=wxID_FRAME1STATICTEXT6,
              label='staticText6', name='staticText6', parent=self,
              pos=wx.Point(584, 144), size=wx.Size(15, 16), style=0)
        self.staticText6.SetLabelText(u'kN')
        self.staticText6.SetToolTipString(u'')

        self.staticBox4 = wx.StaticBox(id=wxID_FRAME1STATICBOX4,
              label='staticBox4', name='staticBox4', parent=self,
              pos=wx.Point(312, 176), size=wx.Size(304, 88), style=0)
        self.staticBox4.SetLabelText(u'Geometria prierezu')
        self.staticBox4.SetToolTipString(u'')

        self.staticText7 = wx.StaticText(id=wxID_FRAME1STATICTEXT7,
              label='staticText7', name='staticText7', parent=self,
              pos=wx.Point(320, 208), size=wx.Size(51, 16), style=0)
        self.staticText7.SetLabelText(u'V\xfd\u0161ka (h):')
        self.staticText7.SetToolTipString(u'')

        self.textCtrl3 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL3, name='textCtrl3',
              parent=self, pos=wx.Point(472, 200), size=wx.Size(104, 23),
              style=0, value='textCtrl3')
        self.textCtrl3.SetLabelText(u'100')
        self.textCtrl3.SetToolTipString(u'V\xfd\u0161ka nosn\xedka v mm')

        self.staticText8 = wx.StaticText(id=wxID_FRAME1STATICTEXT8,
              label='staticText8', name='staticText8', parent=self,
              pos=wx.Point(320, 232), size=wx.Size(46, 16), style=0)
        self.staticText8.SetLabelText(u'\u0160\xedrka (b):')
        self.staticText8.SetToolTipString(u'')

        self.staticText9 = wx.StaticText(id=wxID_FRAME1STATICTEXT9,
              label='staticText9', name='staticText9', parent=self,
              pos=wx.Point(584, 208), size=wx.Size(22, 16), style=0)
        self.staticText9.SetLabelText(u'mm')
        self.staticText9.SetToolTipString(u'')

        self.textCtrl4 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL4, name='textCtrl4',
              parent=self, pos=wx.Point(472, 224), size=wx.Size(104, 23),
              style=0, value='textCtrl4')
        self.textCtrl4.SetToolTipString(u'\u0160\xedrka nosn\xedka v mm')
        self.textCtrl4.SetInsertionPoint(3)
        self.textCtrl4.SetLabelText(u'250')

        self.staticText10 = wx.StaticText(id=wxID_FRAME1STATICTEXT10,
              label='staticText10', name='staticText10', parent=self,
              pos=wx.Point(584, 232), size=wx.Size(22, 16), style=0)
        self.staticText10.SetLabelText(u'mm')
        self.staticText10.SetToolTipString(u'')

        self.staticBox5 = wx.StaticBox(id=wxID_FRAME1STATICBOX5,
              label='staticBox5', name='staticBox5', parent=self,
              pos=wx.Point(312, 264), size=wx.Size(304, 168), style=0)
        self.staticBox5.SetToolTipString(u'Vstupn\xe9 \xfadaje v\xfdstu\u017ee')
        self.staticBox5.SetLabelText(u'Vstupn\xe9 \xfadaje')

        self.staticText11 = wx.StaticText(id=wxID_FRAME1STATICTEXT11,
              label='staticText11', name='staticText11', parent=self,
              pos=wx.Point(320, 296), size=wx.Size(73, 16), style=0)
        self.staticText11.SetToolTipString(u'')
        self.staticText11.SetLabelText(u'Hlavn\xe1 v\xfdstu\u017e')

        self.vystuz_choice = wx.Choice(choices=["6", "8", "10", "12", "14",
              "16"], id=wxID_FRAME1VYSTUZ_CHOICE, name=u'vystuz_choice',
              parent=self, pos=wx.Point(472, 288), size=wx.Size(104, 23),
              style=0)
        self.vystuz_choice.SetToolTipString(u'Priemer pr\xfatov v mm')
        self.vystuz_choice.SetLabelText(u'')
        self.vystuz_choice.SetSelection(4)

        self.staticText12 = wx.StaticText(id=wxID_FRAME1STATICTEXT12,
              label='staticText12', name='staticText12', parent=self,
              pos=wx.Point(584, 296), size=wx.Size(22, 16), style=0)
        self.staticText12.SetLabelText(u'mm')
        self.staticText12.SetToolTipString(u'')

        self.staticText13 = wx.StaticText(id=wxID_FRAME1STATICTEXT13,
              label='staticText13', name='staticText13', parent=self,
              pos=wx.Point(320, 320), size=wx.Size(44, 16), style=0)
        self.staticText13.SetLabelText(u'Strmene')
        self.staticText13.SetToolTipString(u'')

        self.checkBox1 = wx.CheckBox(id=wxID_FRAME1CHECKBOX1,
              label=u'Pou\u017eij\xfa sa', name='checkBox1', parent=self,
              pos=wx.Point(480, 320), size=wx.Size(88, 15), style=0)
        self.checkBox1.SetLabelText(u'Pou\u017eij\xfa sa')
        self.checkBox1.SetValue(True)
        self.checkBox1.SetToolTipString(u'')

        self.strmene_choice = wx.Choice(choices=["6", "8", "10", "12", "14",
              "16"], id=wxID_FRAME1STRMENE_CHOICE, name=u'strmene_choice',
              parent=self, pos=wx.Point(472, 344), size=wx.Size(104, 23),
              style=0)
        self.strmene_choice.SetToolTipString(u'')
        self.strmene_choice.SetSelection(1)
        self.strmene_choice.Bind(wx.EVT_CHOICE, self.OnStrmene_choiceChoice,
              id=wxID_FRAME1STRMENE_CHOICE)

        self.staticText14 = wx.StaticText(id=wxID_FRAME1STATICTEXT14,
              label='staticText14', name='staticText14', parent=self,
              pos=wx.Point(584, 352), size=wx.Size(22, 16), style=0)
        self.staticText14.SetLabelText(u'mm')
        self.staticText14.SetToolTipString(u'')

        self.staticBox6 = wx.StaticBox(id=wxID_FRAME1STATICBOX6,
              label='staticBox6', name='staticBox6', parent=self,
              pos=wx.Point(312, 432), size=wx.Size(304, 88), style=0)
        self.staticBox6.SetToolTipString(u'')
        self.staticBox6.SetLabelText(u'Prostredie')

        self.staticText15 = wx.StaticText(id=wxID_FRAME1STATICTEXT15,
              label='staticText15', name='staticText15', parent=self,
              pos=wx.Point(320, 464), size=wx.Size(93, 16), style=0)
        self.staticText15.SetLabelText(u'Stupe\u0148 prostredia')
        self.staticText15.SetToolTipString(u'')

        self.prostredie_choice = wx.Choice(choices=["X0", "XC1", "XC2", "XC3",
              "XC4", "XD1", "XD2", "XD3"], id=wxID_FRAME1PROSTREDIE_CHOICE,
              name=u'prostredie_choice', parent=self, pos=wx.Point(472, 456),
              size=wx.Size(104, 23), style=0)
        self.prostredie_choice.SetToolTipString(u'Stupe\u0148 prostredia')
        self.prostredie_choice.SetSelection(1)

        self.staticText16 = wx.StaticText(id=wxID_FRAME1STATICTEXT16,
              label='staticText16', name='staticText16', parent=self,
              pos=wx.Point(320, 488), size=wx.Size(136, 16), style=0)
        self.staticText16.SetLabelText(u'Minim\xe1lne krytie (Cnom):')
        self.staticText16.SetToolTipString(u'')

        self.min_krytie_entry = wx.TextCtrl(id=wxID_FRAME1MIN_KRYTIE_ENTRY,
              name=u'min_krytie_entry', parent=self, pos=wx.Point(472, 480),
              size=wx.Size(104, 23), style=0, value='textCtrl5')
        self.min_krytie_entry.SetLabelText(u'10')
        self.min_krytie_entry.SetToolTipString(u'Vypo\u010d\xedtan\xe1 hodnota minim\xe1lneho krytia vv\xfdstu\u017ee bet\xf3nom')
        self.min_krytie_entry.SetEditable(False)

        self.staticText17 = wx.StaticText(id=wxID_FRAME1STATICTEXT17,
              label='staticText17', name='staticText17', parent=self,
              pos=wx.Point(584, 488), size=wx.Size(22, 16), style=0)
        self.staticText17.SetLabelText(u'mm')
        self.staticText17.SetToolTipString(u'')

        self.staticBox7 = wx.StaticBox(id=wxID_FRAME1STATICBOX7,
              label='staticBox7', name='staticBox7', parent=self,
              pos=wx.Point(624, 0), size=wx.Size(336, 184), style=0)
        self.staticBox7.SetLabelText(u'N\xe1vrh plochy v\xfdstu\u017ee')
        self.staticBox7.SetToolTipString(u'')

        self.staticText18 = wx.StaticText(id=wxID_FRAME1STATICTEXT18,
              label='staticText18', name='staticText18', parent=self,
              pos=wx.Point(632, 32), size=wx.Size(135, 16), style=0)
        self.staticText18.SetLabelText(u'\xda\u010dinn\xe1 v\xfd\u0161ka prierezu (d):')
        self.staticText18.SetToolTipString(u'')

        self.staticText19 = wx.StaticText(id=wxID_FRAME1STATICTEXT19,
              label='staticText19', name='staticText19', parent=self,
              pos=wx.Point(632, 56), size=wx.Size(127, 16), style=0)
        self.staticText19.SetToolTipString(u'')
        self.staticText19.SetLabelText(u'V\xfd\u0161ka tla\u010denej \u010dasti (xb):')
        self.staticText19.SetHelpText(u'')

        self.staticText20 = wx.StaticText(id=wxID_FRAME1STATICTEXT20,
              label='staticText20', name='staticText20', parent=self,
              pos=wx.Point(632, 80), size=wx.Size(156, 16), style=0)
        self.staticText20.SetLabelText(u'Skuto\u010dn\xe1 poloha neut. osi (x):')
        self.staticText20.SetToolTipString(u'')

        self.staticText21 = wx.StaticText(id=wxID_FRAME1STATICTEXT21,
              label='staticText21', name='staticText21', parent=self,
              pos=wx.Point(632, 104), size=wx.Size(167, 16), style=0)
        self.staticText21.SetLabelText(u'Limitn\xe1 poloha neut. osi (x,lim):')
        self.staticText21.SetToolTipString(u'')

        self.staticText22 = wx.StaticText(id=wxID_FRAME1STATICTEXT22,
              label='staticText22', name='staticText22', parent=self,
              pos=wx.Point(632, 128), size=wx.Size(176, 16), style=0)
        self.staticText22.SetToolTipString(u'')
        self.staticText22.SetHelpText(u'')
        self.staticText22.SetLabelText(u'Potrebn\xe1 plocha v\xfdstu\u017ee (As,req):')

        self.staticText23 = wx.StaticText(id=wxID_FRAME1STATICTEXT23,
              label='staticText23', name='staticText23', parent=self,
              pos=wx.Point(632, 152), size=wx.Size(172, 16), style=0)
        self.staticText23.SetToolTipString(u'')
        self.staticText23.SetLabelText(u'Min. stupe\u0148 vystu\u017eenia (As,min):')

        self.textCtrl5 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL5, name='textCtrl5',
              parent=self, pos=wx.Point(816, 24), size=wx.Size(96, 23), style=0,
              value='textCtrl5')
        self.textCtrl5.SetToolTipString(u'')
        self.textCtrl5.SetLabelText(u'')
        self.textCtrl5.Enable(False)

        self.textCtrl6 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL6, name='textCtrl6',
              parent=self, pos=wx.Point(816, 48), size=wx.Size(96, 23), style=0,
              value='textCtrl6')
        self.textCtrl6.SetLabelText(u'')
        self.textCtrl6.Enable(False)

        self.textCtrl7 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL7, name='textCtrl7',
              parent=self, pos=wx.Point(816, 72), size=wx.Size(96, 23), style=0,
              value='textCtrl7')
        self.textCtrl7.Enable(False)
        self.textCtrl7.SetLabelText(u'')
        self.textCtrl7.SetToolTipString(u'')

        self.textCtrl8 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL8, name='textCtrl8',
              parent=self, pos=wx.Point(816, 144), size=wx.Size(96, 23),
              style=0, value='textCtrl8')
        self.textCtrl8.SetLabelText(u'')
        self.textCtrl8.SetToolTipString(u'')
        self.textCtrl8.Enable(False)

        self.textCtrl9 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL9, name='textCtrl9',
              parent=self, pos=wx.Point(816, 120), size=wx.Size(96, 23),
              style=0, value='textCtrl9')
        self.textCtrl9.SetLabelText(u'')
        self.textCtrl9.SetToolTipString(u'')
        self.textCtrl9.Enable(False)

        self.textCtrl10 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL10,
              name='textCtrl10', parent=self, pos=wx.Point(816, 96),
              size=wx.Size(96, 23), style=0, value='textCtrl10')
        self.textCtrl10.SetToolTipString(u'')
        self.textCtrl10.Enable(False)
        self.textCtrl10.SetLabelText(u'')

        self.staticText24 = wx.StaticText(id=wxID_FRAME1STATICTEXT24,
              label='staticText24', name='staticText24', parent=self,
              pos=wx.Point(920, 32), size=wx.Size(11, 16), style=0)
        self.staticText24.SetLabelText(u'm')
        self.staticText24.SetToolTipString(u'')

        self.staticText25 = wx.StaticText(id=wxID_FRAME1STATICTEXT25,
              label='staticText25', name='staticText25', parent=self,
              pos=wx.Point(920, 56), size=wx.Size(11, 16), style=0)
        self.staticText25.SetLabelText(u'm')
        self.staticText25.SetToolTipString(u'')

        self.staticText26 = wx.StaticText(id=wxID_FRAME1STATICTEXT26,
              label='staticText26', name='staticText26', parent=self,
              pos=wx.Point(920, 80), size=wx.Size(11, 16), style=0)
        self.staticText26.SetLabelText(u'm')
        self.staticText26.SetToolTipString(u'')

        self.staticText27 = wx.StaticText(id=wxID_FRAME1STATICTEXT27,
              label='staticText27', name='staticText27', parent=self,
              pos=wx.Point(920, 104), size=wx.Size(16, 16), style=0)
        self.staticText27.SetLabelText(u'm')
        self.staticText27.SetToolTipString(u'')

        self.staticText28 = wx.StaticText(id=wxID_FRAME1STATICTEXT28,
              label='staticText28', name='staticText28', parent=self,
              pos=wx.Point(920, 128), size=wx.Size(25, 16), style=0)
        self.staticText28.SetLabelText(u'm^2')
        self.staticText28.SetToolTipString(u'Metre \u0161tvorcov\xe9')

        self.staticText29 = wx.StaticText(id=wxID_FRAME1STATICTEXT29,
              label='staticText29', name='staticText29', parent=self,
              pos=wx.Point(920, 152), size=wx.Size(25, 16), style=0)
        self.staticText29.SetLabelText(u'm^2')
        self.staticText29.SetToolTipString(u'Metre \u0161tvorcov\xe9')

        self.staticText30 = wx.StaticText(id=wxID_FRAME1STATICTEXT30,
              label='staticText30', name='staticText30', parent=self,
              pos=wx.Point(320, 376), size=wx.Size(56, 16), style=0)
        self.staticText30.SetLabelText(u'Kamenivo:')

        self.kamenivo_choice = wx.Choice(choices=["4", "8", "16", "32", "64"],
              id=wxID_FRAME1KAMENIVO_CHOICE, name=u'kamenivo_choice',
              parent=self, pos=wx.Point(472, 368), size=wx.Size(104, 23),
              style=0)
        self.kamenivo_choice.SetSelection(2)
        self.kamenivo_choice.SetToolTipString(u'Max. priemer zrna kameniva')

        self.staticText31 = wx.StaticText(id=wxID_FRAME1STATICTEXT31,
              label='staticText31', name='staticText31', parent=self,
              pos=wx.Point(584, 376), size=wx.Size(22, 16), style=0)
        self.staticText31.SetLabelText(u'mm')
        self.staticText31.SetToolTipString(u'')

        self.staticBox8 = wx.StaticBox(id=wxID_FRAME1STATICBOX8,
              label='staticBox8', name='staticBox8', parent=self,
              pos=wx.Point(624, 184), size=wx.Size(336, 224), style=0)
        self.staticBox8.SetLabelText(u'Dimenzovanie prvku')
        self.staticBox8.SetToolTipString(u'')

        self.staticText32 = wx.StaticText(id=wxID_FRAME1STATICTEXT32,
              label='staticText32', name='staticText32', parent=self,
              pos=wx.Point(632, 216), size=wx.Size(129, 16), style=0)
        self.staticText32.SetLabelText(u'Potrebn\xe1 plocha v\xfdstu\u017ee')
        self.staticText32.SetToolTipString(u'')

        self.textCtrl11 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL11,
              name='textCtrl11', parent=self, pos=wx.Point(816, 208),
              size=wx.Size(96, 24), style=0, value='textCtrl11')
        self.textCtrl11.SetToolTipString(u'')
        self.textCtrl11.SetLabelText(u'5')

        self.staticText33 = wx.StaticText(id=wxID_FRAME1STATICTEXT33,
              label='staticText33', name='staticText33', parent=self,
              pos=wx.Point(920, 216), size=wx.Size(25, 16), style=0)
        self.staticText33.SetLabelText(u'm^2')
        self.staticText33.SetToolTipString(u'V metroch \u0161tvorcov\xfdch')

        self.pruty_list = wx.ListBox(choices=["4x8", "3x10", "2x14", "5x8",
              "4x10", "3x12", "4x12", "3x16"], id=wxID_FRAME1PRUTY_LIST,
              name=u'pruty_list', parent=self, pos=wx.Point(816, 280),
              size=wx.Size(96, 64), style=0)
        self.pruty_list.SetSelection(0)
        self.pruty_list.SetToolTipString(u'Zvo\u013ete si vhodn\xfa v\xfdstu\u017e (po\u010det pr\xfatov x priemer)')

        self.staticText34 = wx.StaticText(id=wxID_FRAME1STATICTEXT34,
              label='staticText34', name='staticText34', parent=self,
              pos=wx.Point(632, 288), size=wx.Size(103, 16), style=0)
        self.staticText34.SetLabelText(u'Navrhovan\xe1 v\xfdstu\u017e:')
        self.staticText34.SetToolTipString(u'')

        self.staticText35 = wx.StaticText(id=wxID_FRAME1STATICTEXT35,
              label='staticText35', name='staticText35', parent=self,
              pos=wx.Point(632, 240), size=wx.Size(58, 16), style=0)
        self.staticText35.SetLabelText(u'Tolerancia:')
        self.staticText35.SetToolTipString(u'')

        self.tolerancia_spin = wx.SpinCtrl(id=wxID_FRAME1TOLERANCIA_SPIN,
              initial=20, max=200, min=0, name=u'tolerancia_spin', parent=self,
              pos=wx.Point(816, 232), size=wx.Size(96, 24),
              style=wx.SP_ARROW_KEYS)
        self.tolerancia_spin.SetToolTipString(u'Tolerancia ktor\xfa program berie do \xfavahy\n(vypo\u010d\xedtan\xe1 plocha + \u010fal\u0161ie mo\u017enosti v r\xe1mci tolerancie v %)')

        self.staticText36 = wx.StaticText(id=wxID_FRAME1STATICTEXT36,
              label='staticText36', name='staticText36', parent=self,
              pos=wx.Point(920, 248), size=wx.Size(10, 16), style=0)
        self.staticText36.SetLabelText(u'%')
        self.staticText36.SetToolTipString(u'')

        self.staticText37 = wx.StaticText(id=wxID_FRAME1STATICTEXT37,
              label='staticText37', name='staticText37', parent=self,
              pos=wx.Point(632, 264), size=wx.Size(152, 16), style=0)
        self.staticText37.SetLabelText(u'Preferovan\xfd priemer v\xfdstu\u017ee:')

        self.vystuz_pref_choice = wx.Choice(choices=["6", "8", "10", "12", "14",
              "16"], id=wxID_FRAME1VYSTUZ_PREF_CHOICE,
              name=u'vystuz_pref_choice', parent=self, pos=wx.Point(816, 256),
              size=wx.Size(96, 23), style=0)
        self.vystuz_pref_choice.SetToolTipString(u'Preferovan\xfd priemer v\xfdstu\u017ee sa v\u017edy objav\xed v navrhovan\xfdch kombin\xe1ciach pr\xfatov')
        self.vystuz_pref_choice.SetSelection(2)

        self.staticText38 = wx.StaticText(id=wxID_FRAME1STATICTEXT38,
              label='staticText38', name='staticText38', parent=self,
              pos=wx.Point(920, 264), size=wx.Size(22, 16), style=0)
        self.staticText38.SetLabelText(u'mm')
        self.staticText38.SetToolTipString(u'')

        self.staticText39 = wx.StaticText(id=wxID_FRAME1STATICTEXT39,
              label='staticText39', name='staticText39', parent=self,
              pos=wx.Point(632, 352), size=wx.Size(81, 16), style=0)
        self.staticText39.SetLabelText(u'Plocha v\xfdstu\u017ee:')
        self.staticText39.SetToolTipString(u'')

        self.textCtrl12 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL12,
              name='textCtrl12', parent=self, pos=wx.Point(816, 344),
              size=wx.Size(96, 23), style=0, value='textCtrl12')
        self.textCtrl12.Enable(False)
        self.textCtrl12.SetToolTipString(u'Zvolen\xe1 plocha v\xfdstu\u017ee')
        self.textCtrl12.SetLabelText(u'')

        self.staticText40 = wx.StaticText(id=wxID_FRAME1STATICTEXT40,
              label='staticText40', name='staticText40', parent=self,
              pos=wx.Point(920, 352), size=wx.Size(31, 16), style=0)
        self.staticText40.SetLabelText(u'cm^2')
        self.staticText40.SetToolTipString(u'')

        self.staticText41 = wx.StaticText(id=wxID_FRAME1STATICTEXT41,
              label='staticText41', name='staticText41', parent=self,
              pos=wx.Point(632, 376), size=wx.Size(0, 16), style=0)
        self.staticText41.SetLabelText(u'')
        self.staticText41.SetToolTipString(u'')

        self.staticText42 = wx.StaticText(id=wxID_FRAME1STATICTEXT42,
              label='staticText42', name='staticText42', parent=self,
              pos=wx.Point(632, 376), size=wx.Size(128, 16), style=0)
        self.staticText42.SetLabelText(u'Krycia vrstva v\xfdstu\u017ee (c):')

        self.krycia_vrstva_entry = wx.TextCtrl(id=wxID_FRAME1KRYCIA_VRSTVA_ENTRY,
              name=u'krycia_vrstva_entry', parent=self, pos=wx.Point(816, 368),
              size=wx.Size(96, 23), style=0, value='textCtrl13')
        self.krycia_vrstva_entry.SetToolTipString(u'Mus\xed by\u0165 v\xe4\u010d\u0161ie nanajv\xfd\u0161 rovn\xe9 Cnom !')
        self.krycia_vrstva_entry.SetLabelText(u'0')
        self.krycia_vrstva_entry.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.staticText43 = wx.StaticText(id=wxID_FRAME1STATICTEXT43,
              label='staticText43', name='staticText43', parent=self,
              pos=wx.Point(920, 376), size=wx.Size(22, 16), style=0)
        self.staticText43.SetLabelText(u'mm')
        self.staticText43.SetToolTipString(u'')

    def __init__(self, parent, verbose):
        self._init_ctrls(parent)
        self.verbose=verbose
        
        self.say("core loaded")

        with open("kektus.conf","r") as subor:
            data=subor.read()
            exec(data)
                        
        self.say("Variables loaded succesfully")

    def recalculate(self):        
        if int(self.min_krytie_entry.GetValue()) > int(self.krycia_vrstva_entry.GetValue()):
            self.krycia_vrstva_entry.SetBackgroundColour(wx.Colour(255, 0, 0))
            say("Attention, Cnom<Cmid")
        else:
            self.krycia_vrstva_entry.SetBackgroundColour(wx.Colour(255, 255, 255))


    def OnStrmene_choiceChoice(self, event):
        self.recalculate()
        event.Skip()

    def say(self, text=""):
        if self.verbose:
            cas=time.ctime().split(" ")[3]
            print "%s - %s"%(cas,text)

if __name__ == '__main__':
    if "-v" in sys.argv:
        verbose=True
    else:
        verbose=False
    app = wx.PySimpleApp()
    frame = create(None, verbose)
    frame.Show()
    app.MainLoop()
