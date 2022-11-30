package com.ssafy.reflection;

public class Test01 {
	public static void main(String[] args) {
		try {
			exam();
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		}
	}

//	클래스를 접근하는 3가지 방법
	private static void exam() throws ClassNotFoundException {
		// 1. 클래스이름.class
		Class<?> clz = Dog.class;
		
		// 2. Class.forName("패키지 포함 클래스명")
		Class<?> clz2 = Class.forName("com.ssafy.reflection.Dog");
		
		// 3. 객체(인스턴스).getClass()
		Dog d = new Dog();
		Class<?> clz3 = d.getClass();
		
		System.out.println(clz == clz2);
		System.out.println(clz2 == clz3);
		
		
		String name = clz.getName(); //기본은 풀패키지명!!
		String sName = clz.getSimpleName();
		
		System.out.println(name);
		System.out.println(sName);

	}
}
