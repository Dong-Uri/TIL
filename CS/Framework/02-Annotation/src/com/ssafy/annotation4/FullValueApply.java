package com.ssafy.annotation4;

public class FullValueApply {
	
	
//	@FullValue(type="1", name="2", value="3")
//	@FullValue(type="1", name="2", "3") //여러개를 같이 쓸때는 value 생략 불가넝
//	@FullValue(name="2", value="3") //type 안써도 에러 x인 이유는 default값이 있기 떄문에.... 
//	@FullValue
	@FullValue("하하호호")
	public void apply() {}
}
