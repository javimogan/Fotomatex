
# 📸 Fotomatex
**_Photo booth using arduino and python_**
<p align="center">
<img src="https://github.com/javimogan/Fotomatex/blob/main/img/horizontal.png?raw=true"
	width = 300
	alt="Fotomatex logo"
	style="float: left; margin-right: 10px;" />
</p>
<p align="center">
<img src="https://github.com/javimogan/Fotomatex/blob/main/img/stock1.jpg?raw=true"
	alt="Fotomatex demo"
	width=350
	style="float: left; margin-right: 10px;" />
<img src="https://github.com/javimogan/Fotomatex/blob/main/img/demo.gif?raw=true"
	alt="Fotomatex demo"
	width=350
	style="float: left; margin-right: 10px;" />
	<img src="https://github.com/javimogan/Fotomatex/blob/main/img/stock.jpg?raw=true"
	alt="Fotomatex demo"
	width=350
	style="float: left; margin-right: 10px;" />
</p>

## Installation
### Desktop
Fotomatex requires the following libraries to run.

```sh
sudo apt install libgphoto2-dev
```
#### Python dependencies
- PyQt5==5.15.4  
- gphoto2==2.2.4  
- serial==0.0.97  
- pyserial==3.5  
- pyudev==0.22.0

To install Python dependencies, run the following command.
```sh
pip3 install -r App/requirements.txt
```
### Arduino
You must connect a button with a pull-down resistor.
You can connect two LEDs, one indicating the unlocked state which allows you to press the button to take a photo, and the other indicating the locked state, in which we will have to wait.


### To run Fotomatex
```sh
python3 App/main.py
```


# 🌚 About author
<!-- About Author -->
<table id="contributors">
	<tr id="info_avatar">
		<td id="javimogan" align="center">
			<a href="https://github.com/javimogan">
				<img src="https://avatars.githubusercontent.com/u/61110500?v=4" width="100px"/>
			</a>
		</td>
	</tr>
	<tr id="info_name">
		<td id="javimogan" align="center">
			<a href="https://github.com/javimogan">
				<strong>Javimogan</strong>
			</a>
		</td>
	</tr>
	<tr id="info_commit">
		<td id="javimogan" align="center">
			<a href="/commits?author=javimogan" title="Developer">
				<span id="role">💻</span>
			</a>
		</td>
	</tr>
</table>
<!-- end About Author -->

