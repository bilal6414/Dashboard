{% extends "base.html" %}

{% block content %}

<div class="container-fluid">
    <form id="friend-form">
        <div class="row">
            {% csrf_token %}
            {% for field in form %}
            <div class="form-group col-4">
                <label class="col-12">{{ field.label }}</label>
                {{ field }}
            </div>
            {% endfor %}
            <input type="submit" class="btn btn-primary" value="Create Friend" />
        </div>
    <form>
</div>
<hr />

<div class="container-fluid">
    <table class="table table-striped table-sm" id="my_friends">
        <thead>
            <tr>
                <th>Nick name</th>
                <th>First name</th>
                <th>Last name</th>
                <th>Likes</th>
                <th>DOB</th>
                <th>lives in</th>
            </tr>
        </thead>
        <tbody>
        {% for friend in friends %}
        <tr>
            <td>{{friend.nick_name}}</td>
            <td>{{friend.first_name}}</td>
            <td>{{friend.last_name}}</td>
            <td>{{friend.likes}}</td>
            <td>{{friend.dob | date:"Y-m-d"}}</td>
            <td>{{friend.lives_in}}</td>
        </tr>
        {% endfor %}
        </tbody>
    </table>

</div>
{% endblock content %}