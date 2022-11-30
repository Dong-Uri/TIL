package com.ssafy.annotation4;

public class SingleApply {
	
	@SingleValue1(value="test")
	@SingleValue2(name="test2")
	public void apply1() {}
	
	
	
//	@SingleValue1	에러발생 default가 없엉
//	@SingleValue2("test3") //불가넝
//	@SingleValue1("test3") //가넝 value 만 생략 가능
//	@SingleValue3			//가넝 
	@SingleValue4			//가넝 
	public void apply2() {}
}
