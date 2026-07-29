use std::io;
fn main(){
    println!("Welcome to the Unit Converter!

Choose a category:

1. Temperature
2. Length

Enter a number:");
loop{
    let mut category = String::new();
    io::stdin().read_line(&mut category).expect("failed to read input");
    let category = category.trim();
    if category == "1"{
        println!("
Welcome to the Temperature Converter!

1. Celsius → Fahrenheit
2. Fahrenheit → Celsius
3. Celsius → Kelvin
4. Kelvin → Celsius
5. Fahrenheit → Kelvin
6. Kelvin → Fahrenheit

Enter a number (1-6):
"); let convertnum: String; loop{
    let mut convertnum_input = String::new();
    io::stdin().read_line(&mut convertnum_input).expect("failed to read input");
    let convertnum_input = convertnum_input.trim();
    if matches!(convertnum_input, "1" | "2" | "3" | "4" | "5" | "6") {
        convertnum = convertnum_input.to_string();
        break;
    } else {
        println!("please make sure to input a number bettween 1 and 6");
    }
    }
    let convertnum = convertnum.as_str();
    let orignal_value: f64;
    loop{
        println!("what number to convert");
        let mut numtoconvert = String::new();
        io::stdin().read_line(&mut numtoconvert).expect("failed to read input");
        let numtoconvert = numtoconvert.trim();
        match numtoconvert.parse::<f64>(){
        Ok(numtoconvert) =>{
        orignal_value = numtoconvert;
        break;
        }
        Err(_) => {
            println!("you didnt enter a valid number");
            println!("please enter a valid number");
        }
        }
    }
    let mut numtoconvert = orignal_value;
    if convertnum == "1" {
        numtoconvert = numtoconvert*1.8;
        numtoconvert = numtoconvert+32.0;
        println!("{orignal_value} degrees Celsius is {} degrees Fahrenheit",numtoconvert);
    }
    else if convertnum == "2" {
        numtoconvert = numtoconvert-32.0;
        numtoconvert = numtoconvert/1.8;
        println!("{} degrees Fahrenheit is {} degrees Celsius",orignal_value,numtoconvert);
    }
    else if convertnum == "3" {
        numtoconvert = numtoconvert+273.15;
        println!("{orignal_value} degrees Celsius is {numtoconvert} degrees Kelvin");
    }
    else if convertnum == "4" {
        numtoconvert = numtoconvert-273.15;
        println!("{} degrees Kelvin is {} degrees Celsius",orignal_value,numtoconvert);
    }
    else if convertnum == "5" {
        numtoconvert = numtoconvert-32.0;
        numtoconvert = numtoconvert/1.8;
        numtoconvert = numtoconvert+273.15;
        println!("{} degrees Fahrenheit is {} degrees Kelvin",orignal_value,numtoconvert);
    }
    else if convertnum == "6" {
        numtoconvert = numtoconvert-273.15;
        numtoconvert = numtoconvert*1.8;
        numtoconvert = numtoconvert+32.0;
        println!("{} degrees Kelvin is {} degrees Fahrenheit",orignal_value,numtoconvert);
    }
    println!("press enter to exit...");
    let mut exit = String::new();
    io::stdin().read_line(&mut exit).unwrap();
    break;


    } else if category == "2"{
        println!("Welcome to the Length Converter!

Choose the unit you want to convert FROM:

1. Millimetres (mm)
2. Centimetres (cm)
3. Metres (m)
4. Kilometres (km)
5. Inches (in)
6. Feet (ft)
7. Yards (yd)
8. Miles (mi)

Enter a number (1-8):");
        break;
    }
    else {
        println!("input a number thats 1 or 2")
    }
}
}
