<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h3>세션에 저장된 정보</h3>
id : <%=session.getAttribute("id") %><br>
name : <%=session.getAttribute("name") %><br>


</body>
</html>