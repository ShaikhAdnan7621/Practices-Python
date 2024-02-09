import kivy
import function
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '500')
Config.set('graphics', 'resizable', '0')
class calculater_desing(GridLayout):
    def new_txt(self,num):
        num= str(num)
        z=self.ids.qs_txt.text
        if num in "+-*/%":
            if z[len(z)-1] in "+-*/%":
                z=z[:-1]
                self.ids.qs_txt.text=f"{num}{z}"
            else:
                self.ids.qs_txt.text=f"{num}{z}"

        if z=="0":
            if num in "+-*/%":
                num=z+num
            self.ids.qs_txt.text=f"{num}"
        else:
            self.ids.qs_txt.text=f"{z}{num}"

    def newest(self):
        z=self.ids.qs_txt.text
        if z != '':
            if "/0" in z:
                self.ids.ans_txt.text=f"#DIVEOR"
                return
            res=function.result_str(z)
            self.ids.ans_txt.text=res
        else:
            self.ids.qs_txt.text="0"

    def back_escape(self):
        z=self.ids.qs_txt.text
        z=z[:-1]
        self.ids.qs_txt.text=f"{z}"
    pass
    
class mainApp(App):
    def build(self):
        return calculater_desing()
mainApp().run()