package com.ssafy.annotation5;

import java.lang.reflect.Method;

public class Test {
	public static void main(String[] args) {
		Class<?> clz = AnnoApply.class;
		
		ClassAnno  cA = clz.getAnnotation(ClassAnno.class);
		RunAnno1  rA = clz.getAnnotation(RunAnno1.class);
		
//		System.out.println(cA); //이건 실행시키면 null이야~
//		System.out.println(rA);
		
		Method[] mArr = clz.getDeclaredMethods();
		
		for(Method m : mArr) {
			RunAnno2 rA2 = m.getAnnotation(RunAnno2.class);
			
			if(rA2 == null) continue;
			
			//이 아래가 실행이 된다는 것은!!
			System.out.println(m.getName());
			System.out.println(rA2.id());
			System.out.println(rA2.msg());
			
		}
		
		
	}
}
