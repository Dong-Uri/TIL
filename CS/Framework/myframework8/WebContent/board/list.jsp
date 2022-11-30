<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>

<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %> 
   
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>게시판</title>
<%@ include file="/include/resource.jsp" %>
</head>
<body>
	<div class="container">
		<%@ include file="/include/header.jsp" %>
		<h2>자유 게시판</h2>
		<hr>
		<div>
			<table class="table text-center">
				<tr>
					<th>번호</th>
					<th>제목</th>
					<th>글쓴이</th>
					<th>조회수</th>
				</tr>
				<c:forEach var="board" items="${list}">
					<tr>
						<td>${board.no}</td>
						<td>${board.title}</td>
						<td>${board.writer}</td>
						<td>${board.viewCnt}</td>
					</tr>
				</c:forEach>
			</table>
			<div class="d-flex justify-content-end">
				<a class="btn btn-outline-danger" href="write-form">등록</a>
			</div>
		</div>
	</div>
</body>
</html>