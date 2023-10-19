fn add(x:i32 , y :i32) ->i64{
	return (x+y).into();
}

fn main() {
	let  x : i32 = 15;
	println!("the value of x+3 is {}",add(x,3));
	println!("Hello, World!");
}
