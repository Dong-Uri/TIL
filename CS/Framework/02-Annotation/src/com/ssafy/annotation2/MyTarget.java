package com.ssafy.annotation2;

import java.lang.annotation.ElementType;
import java.lang.annotation.Target;

//@Target 작성하지 않으면 아무데나 가넝
//@Target(value=ElementType.PARAMETER)
@Target({
	ElementType.TYPE,
	ElementType.FIELD,
	ElementType.METHOD,
	ElementType.LOCAL_VARIABLE,
	ElementType.PARAMETER,
})
public @interface MyTarget {

}
