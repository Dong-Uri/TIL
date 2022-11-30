package com.ssafy.annotation1;

public @interface MyType {
	
	Class<?> classType();
	String stringType();
	int intType();
	Food foodType();
	
	Class<?>[] classArrType();
	String[] stringArrType();
	int[] intArrType();
	Food[] foodArrType();
	
	String[] stringArrDefault() default {"a", "b"};
}
