from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.video import Video
from kivy.core.window import Window

# Add this import at the beginning of your script
from kivy.uix.popup import Popup
import os

class NumerologyNameAnalyzerApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Logo
        logo = Image(source='logo.png')
        layout.add_widget(logo)

        # Input Box
        input_box = TextInput(hint_text='Enter your name')
        layout.add_widget(input_box)

        # Convert Button
        convert_button = Button(text='Convert')
        convert_button.bind(on_press=self.convert_name)
        layout.add_widget(convert_button)

        return layout

    def convert_name(self, instance):
        # Add your name-to-number conversion logic here
        user_name = self.root.children[1].text
        converted_number = self.calculate_number(user_name)
        self.play_video(converted_number)

    def calculate_number(self, name):
        name = name.upper()  # Convert the name to uppercase for consistency
        number_mapping = {
            '1': ['A', 'J', 'S'],
            '2': ['B', 'K', 'T'],
            '3': ['C', 'L', 'U'],
            '4': ['D', 'M', 'V'],
            '5': ['E', 'N', 'W'],
            '6': ['F', 'O', 'X'],
            '7': ['G', 'P', 'Y'],
            '8': ['H', 'Q', 'Z'],
            '9': ['I', 'R']
        }

        special_numbers = ['11', '22', '33']  # Master Numbers

        total = 0

        for letter in name:
            for number, letters in number_mapping.items():
                if letter in letters:
                    total += int(number)
                    break  # Move to the next letter

        while str(total) not in special_numbers and total > 9:
            total = sum(int(digit) for digit in str(total))

        return str(total)

    def play_video(self, number):
        video_filename = f"{number}.mp4"
        video_path = os.path.join(os.path.dirname(__file__), video_filename)

        if os.path.exists(video_path):
            video = Video(source=video_path, state='play')
            video.popup = Popup(title='Numerology Video', content=video, size_hint=(None, None),
                                size=(Window.width * 0.8, Window.height * 0.8))
            video.popup.open()
        else:
            print(f"Video '{video_filename}' not found.")


if __name__ == '__main__':
    NumerologyNameAnalyzerApp().run()
