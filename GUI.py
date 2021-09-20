import PySimpleGUI as sg
form=sg.FlexForm('colors',auto_size_text=False,font=('Helvetica',40))
layout=[[sg.Text('Colors',text_color='black')],
	[sg.Slider(range=(1,9999999999), orientation='h', size=(15,20),background_color='#7BEA0C')],
	[sg.Radio('coffee',group_id=1,background_color='red')],
	[sg.Radio('tea',group_id=1, background_color='blue')],
	[sg.Radio('milk', group_id=1, background_color='cyan')],
	[sg.Radio('OJ', group_id=1, background_color='green')],
	[sg.SimpleButton('Do It!',size=(8,1))],
	]
window=sg.Window('Cat Barn', layout)

button,values=window.Read()

print('value of button is:')
print(button)
print('values of various controls are:')

for i in range(0, 5):
	print(values[i])

