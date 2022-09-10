# KINTER
The easy version of tkinter in python3.
<br>
Try it now.
<br>
Its Intellegent as it installs required packages itself.
<br>
<br><br>
<h2>Which is <i>easier</i> ?</h2>
<hr>
With Traditional Tkinter - 
<br><br>
<code>
import tkinter
<br>
root = tkinter.Tk()
<br>
root.title("Hello World")
<br>
root.geometry("400x500")
<br>
root.iconphoto(False, tkinter.PhotoImage(file="sample.png"))
<br>
root.resizable(0,0)
<br>
root.config(bg="#ffffff")
<br>
root.mainloop()
</code>
<br><br><hr><br>
With kinter -
<br><br>
<code>
import kinter
<br>
kinter.basicAuto()
</code>
<br><br>
or
<br><br>
<code>
import kinter<br><br>

kinter.init()<br>
kinter.setBack("#000000")<br>
kinter.setSize(500, 400)<br>
kinter.setTitle("Its kinter")<br>
kinter.setIcon("sample.png")<br>
kinter.setResizable(False)<br>
kinter.run()<br>
</code>
<br><br>
<h2>Result</h2>
<br><br>
<img src="https://github.com/Sherry65-code/Kinter/blob/main/img.png?raw=true" height="400">
<br><br>
<hr>
<br>
Thank you
