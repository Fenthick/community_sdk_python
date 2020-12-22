from kentik_api.public.query_object import ImageType
from kentik_api.requests_payload.queries_payload import QueryChartResponse


def test_query_chart_response_from_json_success() -> None:
    # given
    json = """{"dataUri": "data:image/png;base64,ImagePNGEncodedBase64"}"""

    # when
    response = QueryChartResponse.from_json(json)

    # then
    assert response.dataUri == "data:image/png;base64,ImagePNGEncodedBase64"


def test_query_chart_response_png_to_query_chart_result_success() -> None:
    # given
    response = QueryChartResponse("data:image/png;base64,ImagePNGEncodedBase64")

    # when
    result = response.to_query_chart_result()

    # then
    assert result.image_type == ImageType.png
    assert result.image_data_base64 == "ImagePNGEncodedBase64"


def test_query_chart_response_jpeg_to_query_chart_result_success() -> None:
    # given
    response = QueryChartResponse("data:image/jpeg;base64,ImageJPEGEncodedBase64")

    # when
    result = response.to_query_chart_result()

    # then
    assert result.image_type == ImageType.jpg
    assert result.image_data_base64 == "ImageJPEGEncodedBase64"


def test_query_chart_response_svg_to_query_chart_result_success() -> None:
    # given
    response = QueryChartResponse("data:image/svg+xml;base64,ImageSVGEncodedBase64")

    # when
    result = response.to_query_chart_result()

    # then
    assert result.image_type == ImageType.svg
    assert result.image_data_base64 == "ImageSVGEncodedBase64"


def test_query_chart_response_pdf_to_query_chart_result_success() -> None:
    # given
    response = QueryChartResponse("data:application/pdf;base64,ApplicationPDFEncodedBase64")

    # when
    result = response.to_query_chart_result()

    # then
    assert result.image_type == ImageType.pdf
    assert result.image_data_base64 == "ApplicationPDFEncodedBase64"


def test_query_chart_response_unknown_format_raises_error() -> None:
    # given
    response = QueryChartResponse("data:image/bmp;base64,ImageBMPEncodedBase64")

    # when
    expected_exception = capture_exception(response.to_query_chart_result)

    # then
    assert isinstance(expected_exception, ValueError)


def test_query_chart_response_unknown_encoding_raises_error() -> None:
    # given
    response = QueryChartResponse("data:image/png;base32,ImagePNGEncodedBase32")

    # when
    expected_exception = capture_exception(response.to_query_chart_result)

    # then
    assert isinstance(expected_exception, ValueError)


def capture_exception(f, *args):
    """ unittest helper. call f and return exception or None """

    try:
        f(*args)
    except Exception as e:
        return e

    return None
