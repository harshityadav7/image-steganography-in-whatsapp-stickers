import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
from PIL import Image
from PIL import ImageDraw
import numpy as np
import cv2
import os


class App:
    def __init__(self, root):
        # setting title
        root.title("undefined")
        # setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        output_location_button = tk.Button(root)
        output_location_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        output_location_button["font"] = ft
        output_location_button["fg"] = "#000000"
        output_location_button["justify"] = "center"
        output_location_button["text"] = "..."
        output_location_button.place(x=500, y=230, width=81, height=30)
        output_location_button["command"] = self.output_location_button_command

        cover_file_button = tk.Button(root)
        cover_file_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        cover_file_button["font"] = ft
        cover_file_button["fg"] = "#000000"
        cover_file_button["justify"] = "center"
        cover_file_button["text"] = "..."
        cover_file_button.place(x=500, y=160, width=81, height=30)
        cover_file_button["command"] = self.cover_file_button_command

        message_file_button = tk.Button(root)
        message_file_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        message_file_button["font"] = ft
        message_file_button["fg"] = "#000000"
        message_file_button["justify"] = "center"
        message_file_button["text"] = "..."
        message_file_button.place(x=500, y=90, width=81, height=30)
        message_file_button["command"] = self.message_file_button_command

        GLabel_201 = tk.Label(root)
        GLabel_201["bg"] = "#25F6EF"
        ft = tkFont.Font(family='Times', size=10)
        GLabel_201["font"] = ft
        GLabel_201["fg"] = "#333333"
        GLabel_201["justify"] = "center"
        GLabel_201["text"] = "Extract from Image"
        GLabel_201.place(x=10, y=310, width=175, height=142)

        stagged_file_button = tk.Button(root)
        stagged_file_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        stagged_file_button["font"] = ft
        stagged_file_button["fg"] = "#000000"
        stagged_file_button["justify"] = "center"
        stagged_file_button["text"] = "..."
        stagged_file_button.place(x=510, y=340, width=78, height=30)
        stagged_file_button["command"] = self.stagged_file_button_command

        output_location2_button = tk.Button(root)
        output_location2_button["activebackground"] = "#0e0e0e"
        output_location2_button["activeforeground"] = "#f8f5f5"
        output_location2_button["bg"] = "#f4eeee"
        ft = tkFont.Font(family='Times', size=10)
        output_location2_button["font"] = ft
        output_location2_button["fg"] = "#070707"
        output_location2_button["justify"] = "center"
        output_location2_button["text"] = "..."
        output_location2_button.place(x=510, y=410, width=79, height=30)
        output_location2_button["command"] = self.output_location2_button_command

        GLabel_457 = tk.Label(root)
        GLabel_457["bg"] = "#25F6EF"
        ft = tkFont.Font(family='Times', size=10)
        GLabel_457["font"] = ft
        GLabel_457["fg"] = "#333333"
        GLabel_457["justify"] = "center"
        GLabel_457["text"] = "Create Sticker"
        GLabel_457.place(x=10, y=110, width=175, height=140)

        convert_button = tk.Button(root)
        convert_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        convert_button["font"] = ft
        convert_button["fg"] = "#000000"
        convert_button["justify"] = "center"
        convert_button["text"] = "Covert"
        convert_button.place(x=250, y=270, width=138, height=30)
        convert_button["command"] = self.convert_button_command

        extract_button = tk.Button(root)
        extract_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        extract_button["font"] = ft
        extract_button["fg"] = "#000000"
        extract_button["justify"] = "center"
        extract_button["text"] = "Extract"
        extract_button.place(x=260, y=460, width=138, height=30)
        extract_button["command"] = self.extract_button_command

        self.message_file_entry = tk.Entry(root)
        self.message_file_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.message_file_entry["font"] = ft
        self.message_file_entry["fg"] = "#333333"
        self.message_file_entry["justify"] = "center"
        self.message_file_entry["text"] = "Message File"
        self.message_file_entry.place(x=200, y=90, width=293, height=30)

        self.cover_file_entry = tk.Entry(root)
        self.cover_file_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.cover_file_entry["font"] = ft
        self.cover_file_entry["fg"] = "#333333"
        self.cover_file_entry["justify"] = "center"
        self.cover_file_entry["text"] = "Cover File"
        self.cover_file_entry.place(x=200, y=160, width=293, height=30)

        output_location_entry = tk.Entry(root)
        output_location_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        output_location_entry["font"] = ft
        output_location_entry["fg"] = "#333333"
        output_location_entry["justify"] = "center"
        output_location_entry["text"] = "Output Location"
        output_location_entry.place(x=200, y=230, width=293, height=30)
        self.output_location_entry = tk.Entry(root, borderwidth="1px", font=ft, fg="#333333")
        # self.output_location_entry.insert(0, "Output Location")

        self.stagged_file_entry = tk.Entry(root)
        self.stagged_file_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.stagged_file_entry["font"] = ft
        self.stagged_file_entry["fg"] = "#333333"
        self.stagged_file_entry["justify"] = "center"
        self.stagged_file_entry["text"] = "Stagged Image"
        self.stagged_file_entry.place(x=200, y=340, width=300, height=30)

        self.stagged_output_location_entry = tk.Entry(root)
        self.stagged_output_location_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.stagged_output_location_entry["font"] = ft
        self.stagged_output_location_entry["fg"] = "#333333"
        self.stagged_output_location_entry["justify"] = "center"
        self.stagged_output_location_entry["text"] = "Stego Ouput File Location"
        self.stagged_output_location_entry.place(x=200, y=410, width=300, height=30)

        GLabel_689 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_689["font"] = ft
        GLabel_689["bg"] = "#F96648"
        GLabel_689["fg"] = "#333333"
        GLabel_689["justify"] = "center"
        GLabel_689["text"] = "Ouput Location"
        GLabel_689.place(x=200, y=380, width=293, height=30)

        GLabel_31 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_31["font"] = ft
        GLabel_31["bg"] = "#F96648"
        GLabel_31["fg"] = "#333333"
        GLabel_31["justify"] = "center"
        GLabel_31["text"] = "Sticker Image"
        GLabel_31.place(x=200, y=310, width=293, height=30)

        GLabel_638 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_638["font"] = ft
        GLabel_638["bg"] = "#F96648"
        GLabel_638["fg"] = "#333333"
        GLabel_638["justify"] = "center"
        GLabel_638["text"] = "Message File"
        GLabel_638.place(x=200, y=60, width=293, height=30)

        GLabel_213 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_213["font"] = ft
        GLabel_213["bg"] = "#F96648"
        GLabel_213["fg"] = "#333333"
        GLabel_213["justify"] = "center"
        GLabel_213["text"] = "Cover File"
        GLabel_213.place(x=200, y=130, width=293, height=30)

        GLabel_547 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_547["font"] = ft
        GLabel_547["bg"] = "#F96648"
        GLabel_547["fg"] = "#333333"
        GLabel_547["justify"] = "center"
        GLabel_547["text"] = "Output Location"
        GLabel_547.place(x=200, y=200, width=293, height=30)

    def output_location_button_command(self):
        file_path = filedialog.askdirectory()
        print(file_path)
        if file_path:
            self.output_location_entry.delete(0, tk.END)  # Clear the current entry
            self.output_location_entry.insert(0, file_path)

    def cover_file_button_command(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")])
        if file_path:
            self.cover_file_entry.delete(0, tk.END)  # Clear the current entry
            self.cover_file_entry.insert(0, file_path)

    def message_file_button_command(self):
        pass

    #     file_path = filedialog.askopenfilename()
    #     if file_path:
    #         self.message_file_entry.delete(0, tk.END)  # Clear the current entry
    #         self.message_file_entry.insert(0, file_path)

    def stagged_file_button_command(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.stagged_file_entry.delete(0, tk.END)  # Clear the current entry
            self.stagged_file_entry.insert(0, file_path)

    def output_location2_button_command(self):
        file_path = filedialog.askdirectory()
        if file_path:
            self.stagged_output_location_entry.delete(0, tk.END)  # Clear the current entry
            self.stagged_output_location_entry.insert(0, file_path)

    def convert_button_command(self):
        message_file_entry_file = self.message_file_entry.get()
        cover_file_entry_file = self.cover_file_entry.get()
        output_location_entry_file = self.output_location_entry.get()
        output_webp_coverFile = ""
        if cover_file_entry_file and output_location_entry_file:
            cover_image = Image.open(cover_file_entry_file)
            desired_width = 512  # Change this to your desired width
            desired_height = 512  # Change this to your desired height

            # Resize the image while maintaining the aspect ratio
            cover_image = cover_image.resize((desired_width, desired_height))

            output_webp_coverFile = f"{output_location_entry_file}/cover_image1.webp"
            cover_image.save(output_webp_coverFile, "webp")

            print(f"Cover image converted and saved to {output_webp_coverFile}")
        else:
            print("Cover file and output location must be provided.")

        # self.hide_text_in_webp(output_webp_coverFile,output_location_entry_file,message_file_entry_file)
        # self.dct_encode(output_webp_coverFile,message_file_entry_file)
        self.encode(output_webp_coverFile, message_file_entry_file)

    def extract_button_command(self):
        stagged_output_location_file = self.stagged_output_location_entry.get()
        stagged_file_entry_file = self.stagged_file_entry.get()
        self.decode(stagged_file_entry_file)

    def decode_to_binary(self, msg):
        msg_type = type(msg)
        if msg_type == str:
            return ''.join([format(ord(i), "08b") for i in msg])
        elif msg_type == bytes or msg_type == np.ndarray:
            return [format(i, "08b") for i in msg]
        elif msg_type == int or msg_type == np.uint8:
            return format(msg, "08b")
        else:
            raise TypeError("Input Type is not supported")

    # Getting the hidden data from the image
    def decodegetData(self, img):
        b_data = ''
        for values in img:
            for pixel in values:
                # convert RGB values to binary format
                r, g, b = self.decode_to_binary(pixel)
                # extracting the data from the LSB of red pixel
                b_data += r[-1]
                # extracting the data from the LSB of green pixel
                b_data += g[-1]
                # extracting the data from the LSB of blue pixel
                b_data += b[-1]

        # split by 8-bits
        bytes_data = [b_data[i:i + 8] for i in range(0, len(b_data), 8)]
        # convert the bits into characters
        decoded_data = ""
        for byte in bytes_data:
            decoded_data += chr(int(byte, 2))
            # check if we have reached the delimiter string
            if decoded_data[-3:] == '###':
                break
        # remove the delimiter string from the final decoded message
        return decoded_data[:-3]

    # Decode the data from the image
    def decode(self, filename):
        img = cv2.imread(filename)
        text = self.decodegetData(img)
        # Print the decoded text into a text file in the same directory as the code file

        with open('Extracted_msg.txt', "w", encoding="utf-8") as f:
            f.write(text)
        # file.write(text)
        # file.close()

    def encode_to_binary(self, msg):
        msg_type = type(msg)
        if msg_type == str:
            return ''.join([format(ord(i), "08b") for i in msg])
        elif msg_type == bytes or msg_type == np.ndarray:
            return [format(i, "08b") for i in msg]
        elif msg_type == int or msg_type == np.uint8:
            return format(msg, "08b")
        else:
            raise TypeError("Input Type is not supported")

    # Hiding the data inside the picture by using LSB(Least Significant Bit) Image Steganography technique
    def encodehidedata(self, img, s_msg):
        # Calculating the maximum bytes that can be encoded
        n_bytes = img.shape[0] * img.shape[1] * 3 // 8

        # Checking if the size of the text provided fits in the image provided
        if len(s_msg) > n_bytes:
            raise ValueError(
                "The size of the secret message is too much. Either reduce the size of the secret message or choose a bigger image.")

        # The delimiter string
        s_msg += '###'

        data_index = 0

        # convert the message in string format to its equivalent binary format
        b_msg = self.encode_to_binary(s_msg)
        len_data = len(b_msg)

        for values in img:
            for pixel in values:

                # convert RGB values to binary format
                r, g, b = self.encode_to_binary(pixel)

                # Change the least significant bit only if there is data to be put in
                if data_index < len_data:
                    # hide the data bit into the LSB of red pixel
                    pixel[0] = int(r[:-1] + b_msg[data_index], 2)
                    data_index += 1
                if data_index < len_data:
                    # hide the data bit into the LSB of green pixel
                    pixel[1] = int(g[:-1] + b_msg[data_index], 2)
                    data_index += 1
                if data_index < len_data:
                    # hide the data bit into the LSB of blue pixel
                    pixel[2] = int(b[:-1] + b_msg[data_index], 2)
                    data_index += 1
                # once the entire data is encoded break out of the loop
                if data_index >= len_data:
                    break
        return img

    # Encode the data into the image
    def encode(self, filename, data):
        image = cv2.imread(filename)
        encoded_img = self.encodehidedata(image, data)
        path = '\\'.join(filename.split('\\')[:-1]) if '\\' in filename else ''
        encode_filename = filename.split('\\')[-1].split('.')[0]
        path += ('\\' + encode_filename) if '\\' in filename else encode_filename
        cv2.imwrite(f'{path}_encoded.webp', encoded_img)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()