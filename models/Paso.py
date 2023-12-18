from odoo import models, fields, api

class Paso(models.Model):
    _name = 'llamador.paso'
    _description = 'Paso de Semana Santa'
    _rec_name = "sNombre"
    # sLocalizacion = fields.Char(string="Localización", required=True)
    # geo_localizacion = fields.Char(string="Ubicación Geoespacial")
    # latitude = fields.Float(string='Latitud')
    # longitude = fields.Float(string='Longitud')
    sNombre = fields.Char('Nombre', required=True)
    iNumeroTramos = fields.Integer('Numero de Tramos',required=True)
    iFilasCuadrilla = fields.Integer('Filas Cuadrilla',required=True)
    iColumnasCuadrilla = fields.Integer('Columnas Cuadrilla',required=True)
    iNumeroCuadrillas = fields.Integer('Numero de Cuadrillas',required=True)
    fPeso = fields.Float('Peso', required=True)
    rel_puntorecorrido= fields.Many2many("llamador.puntorecorrido", string="Puntos de Recorrido")
    rel_tramo = fields.One2many('llamador.tramo', 'rel_paso', string='Tramos')




    iNumeroCostaleros = fields.Integer(compute='_NumeroCostaleros',string="Numero de costaleros",store=True)

    #orm - compute
    
    @api.depends('rel_tramo')
    def _NumeroCostaleros(self):
        for record in self:
            if(record.rel_tramo.rel_papeleta.sTipo == 'tipo3'):
                record.iNumeroCostaleros += 1
    
    #orm - on change
                
    @api.onchange('iFilasCuadrilla')
    def onchange_filasCuadrilla(self):
          if self.iFilasCuadrilla > self.iColumnasCuadrilla and self.sNombre != False    : # el false de dni sirve para que no se ejecute el onchange al pulsar el boton "Create"
               raise models.ValidationError('Las filas deben ser menores o iguales a las columnas.')
    @api.onchange('iColumnasCuadrilla')
    def onchange_columnasCuadrilla(self):
          if self.iColumnasCuadrilla > self.iFilasCuadrilla and self.sNombre != False    : # el false de dni sirve para que no se ejecute el onchange al pulsar el boton "Create"
               raise models.ValidationError('Las columnas deben ser menores o iguales a las columnas.')
    @api.onchange('fPeso')
    def onchange_peso(self):
          if self.fPeso <=0 and self.sNombre != False    : # el false de dni sirve para que no se ejecute el onchange al pulsar el boton "Create"
               raise models.ValidationError('El peso debe ser positivo.')






    html_content = fields.Html(string='HTML') 

    _html_head = """
    <head>
        <meta charset='utf-8'>
        <meta http-equiv='X-UA-Compatible' content='IE=edge'>
        <title>TSI EJERCICIO 1.2</title>
        <meta name='viewport' content='width=device-width, initial-scale=1'>
        <link rel='stylesheet' type='text/css' media='screen' href='main.css'>
    </head>
    """

    _html_body = """
    <body>
        <h1>Mapa Sevilla</h1>
        <div id="googleMap" style="width:100%;height:400px;"></div>

        <script>
            const iconBase ="https://developers.google.com/maps/documentation/javascript/examples/full/images/";
            function myMap() {
                var mapProp= {
                    center:new google.maps.LatLng(37.3828300,-5.9731700),
                    mapId:'972c534fcb452a5e',
                    zoom:12,
                };
                
                var map = new google.maps.Map(document.getElementById("googleMap"),mapProp);
                new google.maps.Marker({
                    position: { lat: 37.3828300, lng: -5.9731700 },
                    map,
                    icon:iconBase + "info-i_maps.png",
                    title: "INFORMASION DEL MAPA",
                });
            }
        </script>

        <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBZgkbeAVF_6hbi4uK_m6_bFdlzeVA8RYs&callback=myMap"></script>
    </body>
    """

    html_content = fields.Html(string='Contenido HTML', default=_html_head + _html_body)

    
