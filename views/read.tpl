<head>
<style>
table {
  border-collapse: collapse;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

</style>
</head>
<body>

<p>Read</p>

<table>
    %for row in rows:
    <tr>
        <th>Todo Message</th>
        <th>Created Date</th>
        <th>Updated Date</th>
    </tr>
    <tr>
        %for item in row[1:]:
            <td>{{item}}</td>
        %end
    </tr>
   %end
</table>

</body>
</html>
