<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
   
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>회원</title>
<%@ include file="/WEB-INF/views/include/resource.jsp" %>
</head>
<body>
	<div class="container">
		<%@ include file="/WEB-INF/views/include/header.jsp" %>
		<h2>싸피 회원 - 목록 페이지</h2>
		<hr>
		<div>
			<table class="table text-center">
				<tr>
					<th>아이디</th>
					<th>이름</th>
					<th>이메일</th>
				</tr>
				<c:forEach items="${list}" var="user">
					<tr>
						<td>${user.id}</td>
						<td>${user.name}</td>
						<td>${user.email}</td>
					</tr>
				</c:forEach>
			</table>
			<div class="d-flex justify-content-end">
				<a class="btn btn-outline-danger" href="join-form">가입</a>
			</div>
		</div>
	</div>
</body>
</html>