<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>글작성</title>
<%@ include file="/include/resource.jsp" %>
</head>
<body>
	<div class="container">
		<%@ include file="/include/header.jsp" %>
		<h2>회원 - 가입 페이지</h2>
		<form action="${pageContext.request.contextPath}/user" method="POST">
			<input type="hidden" name="act" value="join">
			<div class="mb-3">
			  <label for="id" class="form-label">아이디</label>
			  <input type="text" class="form-control" id="id" name="id">
			</div>
			<div class="mb-3">
			  <label for="name" class="form-label">이름</label>
			  <input type="text" class="form-control" id="name" name="name">
			</div>
			<div class="mb-3">
			  <label for="password" class="form-label">패스워드</label>
			  <input type="password" class="form-control" id="password" name="password">
			</div>
			<div class="mb-3">
			  <label for="email" class="form-label">이메일</label>
			  <input type="text" class="form-control" id="email" name="email">
			</div>
			<button class="btn btn-primary">가입</button>
		</form>
	</div>
</body>
</html>