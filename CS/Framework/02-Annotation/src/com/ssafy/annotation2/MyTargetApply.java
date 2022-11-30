package com.ssafy.annotation2;

@MyTarget
public class MyTargetApply {
	@MyTarget
	private String msg;

	@MyTarget
	public void call() {
	}

	public void test(@MyTarget String msg) {
		@MyTarget
		int val = 100;
	}
}
