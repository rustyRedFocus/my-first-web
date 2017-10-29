function sayHello() {
   window.alert("Hello World!")
}

function confirmDelete() {
	var txt;
	var r = window.confirm("Really?");
	if (r == true) {
		txt = "You pressed YES!";
	} else {
		txt = "You pressed NO!"
		location.reload();
	}
}

