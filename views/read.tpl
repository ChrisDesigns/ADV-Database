<p>Read</p>

<table>
    %for row in rows:
    <tr>
        <th>{{row[0]}}</th>
    </tr>
    <tr>
        %for item in row[1:]:
            <td>{{item}}</td>
        %end
    </tr>
   %end
</table>


