import cv2 as cv
from flask import Flask, Response

video = cv.VideoCapture(0)
app = Flask("__name__")


def video_stream():
    while True:
        ret, frame = video.read()
        if not ret:
            break
        else:
            ret, buffer = cv.imencode(".jpeg", frame)
            frame = buffer.tobytes()
            yield (
                b" --frame\r\n" b"Content-type: imgae/jpeg\r\n\r\n" + frame + b"\r\n"
            )


@app.route("/video_feed")
def video_feed():
    return Response(
        video_stream(), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


app.run(host="0.0.0.0", port=5000, debug=False)
