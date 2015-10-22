var task = {
    delete: function(event) {
        $.ajax({
            url: event.target.dataset.taskPath,
            settings: {
                async: false
            },
            method: 'DELETE',
            success: function() {
                $('#' + event.target.dataset.taskElementId).remove();
            }
        })
    }
};

$( document ).ready(function() {
    $('.btn-delete').click(task.delete)
});
