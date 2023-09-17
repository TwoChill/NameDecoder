import os
from kivy.uix.video import Video
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen

# Add this import at the beginning of your script
from kivy.uix.popup import Popup


class NumerologyNameAnalyzerApp(MDApp):
    """
    The main application class for NumerologyNameAnalyzer.

    This class defines the structure and behavior of the NumerologyNameAnalyzer app.
    It includes the user interface setup, name-to-number conversion logic, and video playback.

    Attributes:
        None

    Methods:
        - build(self): Build the app's user interface.
        - convert_name(self, instance): Handle name conversion and video playback.
        - calculate_number(self, name): Calculate the numerology number for a given name.
        - play_video(self, number): Play the associated video explanation.
    """

    def build(self):
        """
        Build the user interface of the NumerologyNameAnalyzer app.

        This method constructs the app's user interface, including a logo, input box,
        and 'Convert' button.

        Parameters:
            self: The NumerologyNameAnalyzerApp instance.

        Returns:
            layout (BoxLayout): The root layout of the app's user interface.
        """
        # Customize the color palette
        self.theme_cls.primary_palette = "Purple"  # Set the primary color
        self.theme_cls.primary_hue = "400"  # Choose the hue (e.g., "400")
        self.theme_cls.theme_style = "Dark"  # Choose the dark theme

        screen = MDScreen()

        # Create a BoxLayout for content with a vertical orientation
        content = BoxLayout(orientation="vertical")

        # Create a custom toolbar using a BoxLayout
        toolbar = BoxLayout(
            orientation="horizontal",
            size_hint=(1, None),
            height=56,  # Adjust the height as needed
            spacing=10,
        )
        title_label = Label(
            text="Numerology Name Analyzer",
            size_hint_x=None,
            width=Window.width,  # Adjust the width as needed
            bold=True,
            color=(1, 1, 1, 1),  # Set the text color to white (R,G,B,A)
        )

        toolbar.add_widget(title_label)

        # Create a BoxLayout for the middle widget (name input and video) with a vertical orientation
        middle_widget = BoxLayout(orientation="vertical", size_hint=(1, None), height=300)

        # Create an MDTextField for name input with a customized line color
        name_input = MDTextField(
            hint_text="Enter your name",
        )
        name_input.line_color = self.theme_cls.primary_color  # Set the line color

        # Create an MDRaisedButton for conversion with a customized color
        convert_button = MDRaisedButton(
            text="Convert",
            on_release=self.convert_name,
            md_bg_color=self.theme_cls.primary_color,  # Use the primary color
        )

        middle_widget.add_widget(name_input)  # Add the name input field here
        middle_widget.add_widget(convert_button)

        # Create an MDLabel for displaying results
        self.result_label = MDLabel()
        middle_widget.add_widget(self.result_label)

        # Add the middle widget to the content layout
        content.add_widget(toolbar)
        content.add_widget(middle_widget)

        screen.add_widget(content)
        return screen

    def convert_name(self, instance):
        """
        Handle name conversion and video playback.

        This method is triggered when the user clicks the 'Convert' button. It retrieves
        the user-entered name, calculates the numerology number, and plays the associated
        video explanation.

        Parameters:
            self: The NumerologyNameAnalyzerApp instance.
            instance: The button instance that triggered the event.

        Returns:
            None
        """

        user_name = self.root.children[1].text
        converted_number = self.calculate_number(user_name)
        self.result_label.text = f"Numerology Number: {converted_number}"
        self.play_video(converted_number)

    def calculate_number(self, name):
        """
        Calculate the numerology number for a given name.

        This method takes a user-entered name and calculates the corresponding numerology
        number based on Pythagorean numerology and the provided vibrational correlations.

        Parameters:
            self: The NumerologyNameAnalyzerApp instance.
            name (str): The user-entered name.

        Returns:
            str: The numerology number as a string.
        """
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
        """
        Play the associated video explanation for a numerology number.

        This method plays the video explanation associated with the numerology number
        provided as an argument. It retrieves and displays the video from the 'partend'
        directory.

        Parameters:
            self: The NumerologyNameAnalyzerApp instance.
            number (str): The numerology number as a string.

        Returns:
            None
        """
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
