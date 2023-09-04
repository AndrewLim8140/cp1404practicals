from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
MULTIPLIER=1.609340
class ConverterApp(App):
    input_miles=StringProperty()

    def build(self):
        self.title = "Miles Converter"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def miles_increment(self,miles,increments):
        try:
            miles = int(miles) + increments
            self.root.ids.input_miles.text = str(miles)
        except ValueError:
            miles = 0 + increments
            self.root.ids.input_miles.text = str(miles)
            self.root.ids.output_results.text = '0.0'



    def miles_conversion(self,miles):
        try:
            km = int(miles) * MULTIPLIER
            self.root.ids.output_results.text = str(km)

        except ValueError:
             self.root.ids.output_results.text = '0.0'

ConverterApp().run()