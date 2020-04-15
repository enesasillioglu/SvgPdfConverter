from wsgiref.simple_server import make_server

import falcon
import cairosvg


class Svg2PdfConverter:
    def on_post(self, req, resp):
        svg = req.media['svg']
        resp.downloadable_as = 'export.pdf'
        resp.content_type = 'application/pdf'
        pdf = cairosvg.svg2pdf(bytestring=svg)
        resp.status = falcon.HTTP_200
        resp.data = pdf
    def on_get(self, req, resp):
        example = '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1920" height="569" style="border: 1px solid black; overflow: hidden;"><defs /><g id="container" transform="matrix(1.0000,0.0000,0.0000,1.0000,960.0000,284.50)"><g id="container_1" transform="matrix(0.0131,0.0000,0.0000,0.0131,0.0000,0.00)"><g id="container_2" /><g id="container_3" /><g id="container_4" /><g id="container_5" /><g id="container_6" /><g id="container_7" /><g id="container_8" /></g><g id="container_9" transform="matrix(0.0131,0.0000,0.0000,0.0131,0.0000,0.00)"><g id="container_10" /><g id="container_11" /><g id="container_12"><g id="object-Pipe-7"><g id="container_13"><path d="M -249 -119L -66 -119.00000000000003" style="fill:none;stroke:#ffc107;stroke-width:4.22;stroke-linecap:butt;stroke-miterlimit:10;" id="shape" /><path d="M -249 -119L -66 -119.00000000000003" style="fill:none;stroke:#646464;stroke-opacity:0.01;stroke-width:24.22;stroke-linecap:round;stroke-miterlimit:10;stroke-dasharray:30,1;" id="shape_1" /></g></g></g><g id="container_14"><g id="object-GasMeter-4"><g id="shape_2" transform="matrix(1.0000,0.0000,0.0000,1.0000,-271.5000,-119.00)"><rect x="0" y="17" width="30" height="30" style="fill:none;stroke:#15b2c8;stroke-linecap:butt;stroke-miterlimit:10;" /><path d="M 7.5 0L 7.5 17M 22.5 0L 22.5 17" style="fill:none;stroke:#15b2c8;stroke-linecap:butt;stroke-miterlimit:10;" /></g><g id="container_15"><text id="text" opacity="0.9000" transform="matrix(1.0000,0.0000,0.0000,1.0000,-363.0000,-56.30)" fill="#ff7700" font-size="13px" font-family="Arial" font-weight="normal"><tspan x="0" dy="12.994921875" dx="0">Sayaç</tspan><tspan x="0" dy="12.994921875" dx="0">Dükkan (Ticari Amaçlı)</tspan><tspan x="0" dy="12.994921875" dx="0" /></text><path d="M -264 -119L -363 -68" style="fill:none;stroke:#ff7700;stroke-linecap:butt;stroke-miterlimit:10;stroke-dasharray:8,10;" id="shape_3" opacity="0.5000" /></g><text id="text_1" transform="matrix(1.0000,0.0000,0.0000,1.0000,-265.1709,-81.80)" fill="#646464" font-size="13px" font-family="Arial" font-weight="normal">G4</text></g></g><g id="container_16"><g id="object-Valve-3"><path d="M 0 0L 15 15L 15 0L 0 15L 0 0" style="fill:#646464;fill-opacity:0.1;stroke:#15b2c8;stroke-linecap:butt;stroke-miterlimit:10;" id="shape_4" transform="matrix(-1.0000,0.0000,-0.0000,-1.0000,-256.5000,-111.50)" /></g><g id="object-Valve-13"><path d="M 0 0L 15 15L 15 0L 0 15L 0 0" style="fill:none;stroke:#15b2c8;stroke-linecap:butt;stroke-miterlimit:10;" id="shape_5" transform="matrix(1.0000,-0.0000,0.0000,1.0599,-73.5000,-126.95)" /><g id="container_17"><text id="text_2" opacity="0.9000" transform="matrix(1.0000,0.0000,0.0000,1.0000,-51.0000,-92.30)" fill="#ff7700" font-size="13px" font-family="Arial" font-weight="normal"><tspan x="0" dy="12.994921875" dx="0" /><tspan x="0" dy="12.994921875" dx="0" /></text><path d="M -66 -119.00000000000003L -51 -104.00000000000003" style="fill:none;stroke:#ff7700;stroke-linecap:butt;stroke-miterlimit:10;stroke-dasharray:8,10;" id="shape_6" opacity="0.5000" /></g></g></g><g id="container_18"><g id="object-Cooker-12"><g id="shape_7" transform="matrix(1.0000,0.0000,0.0000,1.0000,-82.5000,-99.00)"><g style="fill:none;stroke:#ff0000;stroke-width:2;stroke-linecap:butt;stroke-miterlimit:10;"><rect x="0" y="0" width="35" height="35" rx="3" /><path d="M 15.75 8.75" /><circle cx="10.75" cy="8.75" r="3.5" /><path d="M 29.25 8.75" /><circle cx="24.25" cy="8.75" r="3.5" /><path d="M 15.75 26.25" /><circle cx="10.75" cy="26.25" r="3.5" /><path d="M 29.25 26.25" /><circle cx="24.25" cy="26.25" r="3.5" /></g><path d="M 3 0L 3 35M 32 0L 32 35" style="fill:none;stroke:#ff0000;stroke-linecap:butt;stroke-miterlimit:10;" /></g><path d="M -65 -81.5L -66 -119.00000000000003" style="fill:none;stroke:#33cc33;" id="shape_8" /><g id="container_19"><text id="text_3" opacity="0.9000" transform="matrix(1.0000,0.0000,0.0000,1.0000,-50.0000,-54.80)" fill="#ff7700" font-size="13px" font-family="Arial" font-weight="normal"><tspan x="0" dy="12.994921875" dx="0">Evsel Ocak</tspan><tspan x="0" dy="12.994921875" dx="0">CE Belgeli</tspan><tspan x="0" dy="12.994921875" dx="0">13200 Kcal/h 15.35 KW</tspan></text><path d="M -65 -81.5L -50 -66.5" style="fill:none;stroke:#ff7700;stroke-linecap:butt;stroke-miterlimit:10;stroke-dasharray:8,10;" id="shape_9" opacity="0.5000" /></g></g></g><g id="container_20"><g id="container_21"><g id="container_22"><text id="text_4" opacity="0.9000" transform="matrix(1.0000,0.0000,0.0000,1.0000,-152.5000,-81.30)" fill="rgb(255,193,7)" text-anchor="middle" font-size="13px" font-family="Arial" font-weight="normal"><tspan x="0" dy="12.994921875" dx="0">(1)</tspan><tspan x="0" dy="12.994921875" dx="0">1.6m³/h</tspan><tspan x="0" dy="12.994921875" dx="0">1.83m</tspan><tspan x="0" dy="12.994921875" dx="0">DN20</tspan></text><path d="M -157.5 -119.00000000000001L -152.5 -93.00000000000001" style="fill:none;stroke:#ffc107;stroke-linecap:butt;stroke-miterlimit:10;stroke-dasharray:8,10;" id="shape_10" opacity="0.5000" /></g></g></g><g id="container_23"><g id="object-BranchPipe-2"><g id="object-BranchPipe-2_1"><path d="M -313 -119L -264 -119" style="fill:none;stroke:#15b2c8;stroke-width:2;stroke-linecap:butt;stroke-miterlimit:10;stroke-dasharray:4,4;stroke-dashoffset:4;" id="shape_11" /><path d="M -313 -119L -264 -119Z" style="fill:none;stroke:#646464;stroke-opacity:0.01;stroke-width:8;stroke-linecap:butt;stroke-miterlimit:10;" id="shape_12" /></g></g></g><g id="container_24" /><g id="container_25"><g id="object-InstalmentPoint-0" /><g id="object-InstalmentPoint-1" /><g id="object-InstalmentPoint-5" /><g id="object-InstalmentPoint-6" /></g></g></g></svg>'
        resp.downloadable_as = 'export.pdf'
        resp.content_type = 'application/pdf'
        pdf = cairosvg.svg2pdf(bytestring=example)
        resp.status = falcon.HTTP_200
        resp.data = pdf


api = falcon.API()

converter = Svg2PdfConverter()

api.add_route('/convert', converter)

if __name__ == '__main__':
    with make_server('', 8000, api) as httpd:
        print('Serving on port 8000...')

        # Serve until process is killed
        httpd.serve_forever()
