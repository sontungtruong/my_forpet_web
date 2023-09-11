# petnet
{% if request.user.userprofile.is_vendor %}
                    <a href="{% url 'my_store' %}" class="py-2 px-2 bg-teal-800 text-white rounded-xl hover:bg-teal-900">
                        My store
                    </a>    
                {% endif %}