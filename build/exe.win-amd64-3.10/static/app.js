$(document).ready(() => {
    window.onload = function () {
        $('#close').fadeOut(2000, function () {
            $('#close').css("opacity", "0").remove();
        });
    }

    var scrollTop_of_prompt = () => {
        var elem = document.getElementById('prompt');
        elem.scrollTop = elem.scrollHeight;
    }

    var errorMsg_display = (msg) => {
        $(".prompt_content").append("<p style='color:#ff5454'>" + msg + "</p>")
        scrollTop_of_prompt()
        $(".downloading_loader").removeClass("dwnLoader_active")
    }

    var succesMsg_display = (msg) => {
        $(".prompt_content").append("<p style='color:#000000'>" + msg + "</p>")
        scrollTop_of_prompt()

        $(".image_inp").val('')
        $(".image_num_inp").val('')
        $(".image_folder_destination_inp").val('')


        $(".downloading_loader").removeClass("dwnLoader_active")
    }

    var normalMsg_display = (msg) => {
        $(".prompt_content").append("<p>" + msg + "</p>")
        scrollTop_of_prompt()
    }


    var connectMsg_display = (msg) => {
        $(".prompt_content").append("<p style='color:#00ff00'>" + msg + "</p>")
        scrollTop_of_prompt()
    }

    var connect_to_server = (img_name_inp, img_num_inp, img_des_path) => {
        try {
            $(".downloading_loader").addClass("dwnLoader_active")


            $.post("/get_data", {
                image_data: img_name_inp,
                image_count: img_num_inp,
                image_destination_folder: img_des_path,
            }, function (data, status) {
                succesMsg_display(data)
            }).fail(() => {
                errorMsg_display("Sever Error")
            })

        } catch (e) {
            errorMsg_display(`<em>Server Error: ${e}</em><br>`)
        }
    }


    $(".scrap_btn").click(() => {

        img_name_inp = $(".image_inp").val()
        img_num_inp = $(".image_num_inp").val()

        img_des_path = $(".image_folder_destination_inp").val()


        if (img_name_inp && img_num_inp.length > 0 && img_num_inp != 0 && img_des_path) {
            if (img_des_path.match(/^[A-Z]\:\\*/gm) != null) {
                img_des_path = $(".image_folder_destination_inp").val()
                img_des_path = img_des_path.endsWith('\\') ? img_des_path.slice(0, -1) : img_des_path

                normalMsg_display(`<strong>Input:</strong>- \tImage Name:\t ${img_name_inp},\t Count: ${img_num_inp},<br> Destination: ${img_des_path}`)
                connect_to_server(img_name_inp, img_num_inp, img_des_path)
            } else {
                errorMsg_display("Error: Invalid folder path... 🤨")
            }
        } else if (img_name_inp && img_num_inp.length > 0 && img_num_inp != 0) {

            normalMsg_display(`<strong>Input:</strong>- \tImage Name:\t ${img_name_inp},\t Count: ${img_num_inp}`)
            connect_to_server(img_name_inp, img_num_inp, img_des_path)

        } else {
            if (!img_name_inp) {
                errorMsg_display("Error: No image name found... 😬")
            } else if (img_num_inp.length == 0) {
                errorMsg_display("Error: Give the number of images to download... 😒")
            } else if (img_num_inp == 0) {
                errorMsg_display("Error: U want us to download zero images... 🤬")
            }
        }

    })
})