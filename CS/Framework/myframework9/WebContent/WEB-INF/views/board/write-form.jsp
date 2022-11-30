<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>글작성</title>
<%@ include file="/WEB-INF/views/include/resource.jsp" %>
</head>
<body>
	<div class="container">
		<%@ include file="/WEB-INF/views/include/header.jsp" %>
		<h2>글 작성</h2>
		<form action="write" method="post">
			<input type="hidden" name="act" value="write">
			<div class="mb-3">
			  <label for="title" class="form-label">글제목</label>
			  <input type="text" class="form-control" id="title" name="title">
			</div>
			<div class="mb-3">
			  <label for="writer" class="form-label">글쓴이</label>
			  <input type="text" class="form-control" id="writer" name="writer">
			</div>
			<div class="mb-3">
			  <label for="content" class="form-label">글내용</label>
			  <textarea class="form-control" id="content" name="content" rows="10"></textarea>
			</div>
			<button class="btn btn-primary">등록</button>
		</form>
	</div>
</body>
</html>