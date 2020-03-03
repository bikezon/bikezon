/* File for AJAX related js scripts */

/* Test button to test that AJAX works - won't actually do anything*/
$(document)
    .ready(function() {
      $('#like_btn')
          .click(function() {
            var categoryIdVar;
            categoryIdVar = $(this).attr('data-categoryid');
            $.get('/app/like_category/', {'category_id': categoryIdVar},
                  function(data) {
                    $('#like_count').html(data);
                    $('#like_btn').hide();
                  })
          });
    });