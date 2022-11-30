package com.ssafy.annotation5;

@ClassAnno("클래스 설정")
@RunAnno1("런타임 설정")
public class AnnoApply {
	@RunAnno2(id="ssafy", msg="Hell~o")
	public void info() {}
	
	public void call() {}
}
