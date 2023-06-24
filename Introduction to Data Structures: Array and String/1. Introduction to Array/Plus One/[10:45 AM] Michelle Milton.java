[10:45 AM] Michelle Milton
    package com.ebsco.resourcemanagement.shared.lti.controller.Book;
import java.util.List;
import java.util.Random;
import lombok.*;
public class Cycle {​​
@Getter @Setter private Frame frame;
@Getter @Setter private List<Wheel> wheels;
@Getter private final String name = "default";
public Cycle(){​​}​​
public Cycle(Frame frame, List<Wheel> wheels, String name) {​​
this.frame = frame;
this.wheels = wheels;
this.name = name;
}​​
protected String colors(){​​
if (frame.colors.size() > 2) {​​
return "too many colors";
}​​ else if(frame.colors.size() == 0) {​​
return "no colors";
}​​ else {​​
return "not enough colors";
}​​
}​​
/**
* Generate a random string that has a length of 20
* @return a random string
*/
protected static String generateName() {​​
Random rnd = new Random();
var inputChar = "abcdefghijklmnopqrstuvwx1234567890";
var sb = new StringBuilder();
// Use rnd.nextFloat() generates random value between 0.0 and 1.0
while (sb.length() < 20) {​​
var index = (int) (rnd.nextFloat() * inputChar.length());
//Random index is chosen and string of length 20 is formed
sb.append(inputChar.charAt(index));
}​​
return sb.toString();
}​​
}​​
@Data
public class Frame {​​
List<String> colors;
List<String> materials;
}​​
@Data
public class Wheel {​​
List<String> colors;
List<String> materials;
}​​
