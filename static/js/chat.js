(function () {
  $(function () {
    function Message({ text: text1, message_side: message_side1 }) {
      this.text = text1;
      this.message_side = message_side1;
      this.draw = () => {
        var $message = $($(".message_template").clone().html());
        $message.addClass(this.message_side).find(".text").text(this.text);
        $(".messages").append($message);
        return setTimeout(function () {
          return $message.addClass("appeared");
        }, 0);
      };
      return this;
    }

    function showMessage(text, message_side) {
      if (text.trim() === "") {
        return;
      }
      $(".message_input").val("");
      const $messages = $(".messages");
      const message = new Message({ text, message_side });

      message.draw();
      $messages.animate(
        {
          scrollTop: $messages.prop("scrollHeight"),
        },
        300
      );
    }
    const showReceiveMessage = (text) => showMessage(text, "right");
    const showTransferMessage = (text) => showMessage(text, "left");

    getAnswer('', true)
      .then((response) => {
        response?.data?.map((conversation) => {
          showReceiveMessage(conversation?.question);
          showTransferMessage(conversation?.answer);
        });
      })
      .catch((error) => {});

    const sendMessage = () => {
      const inputText = $(".message_input").val();

      showReceiveMessage(inputText);
      getAnswer(inputText)
        .then((response) => {
          response?.data?.map((conversation) => {
            showTransferMessage(conversation?.answer);
          });
        })
        .catch((error) => {});
    };

    $(".message_input").keyup(function (e) {
      if (e.which === 13) {
        // enter key
        sendMessage();
      }
    });

    $(".send_message").click(function (e) {
      sendMessage();
    });
  });
}).call(this);
