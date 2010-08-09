$(document).ready(function() {
	
	$('#add').click(function() {
		$.post("/deploy/ajax/add_env/",
			{
				project:	$('#id_project').val(),
				'function':	$('#id_function').val(),
				name:		$('#id_name').val(),
				about:		$('#id_about').val()
			},
			function(json) {
				if (json.error == 0) {
					$('ul.envs').append("<li><img src='/static/images/remove.gif' class='remove_env' id='"+json.id+"'> "+ $('input#id_name').val() +" ("+ $('select#id_function option:selected').text() +")</li>");
					
					$("select#id_function option[value='"+ $('select#id_function option:selected').val() +"']").remove();
					
					$('input#id_name').val("");
					$('#id_about').val("");
					$('select#id_function').val("");
					
					$('div#show_env_warning').slideUp(400);
				}
			}, "json"
		);
	});
	
	$("img.remove_env").live("click", function(event) {
		obj = $(this);
	
		$.post("/deploy/ajax/delete_env/",
			{
				env:	obj.attr('id')
			},
			function(json) {
				if (json.error == 0) {
					obj.parent().slideUp(500).remove();

					$("select#id_function").append("<option value='"+ json.id +"'>"+ json.func +"</option>");
					
					if ($('ul.envs').children().length == 0) {
						$('div#show_env_warning').slideDown(400);
					}
				}
			}, "json"
		);
	});
	
	
});
