curl --location 'https://data.covid19.go.id/public/api/update.json'
{
    "data": {
        "id": 1,
        "jumlah_odp": 152151,
        "jumlah_pdp": 0,
        "total_spesimen": 21756322,
        "total_spesimen_negatif": 15186818
    },
    "update": {
        "penambahan": {
            "jumlah_positif": 36197,
            "jumlah_meninggal": 1007,
            "jumlah_sembuh": 32615,
            "jumlah_dirawat": 2575,
            "tanggal": "2021-07-11",
            "created": "2021-07-11 15:43:32"
        },
        "harian": [
            {previous data},
            {
                "key_as_string": "2021-07-11T00:00:00.000Z",
                "key": 1625961600000,
                "doc_count": 1,
                "jumlah_meninggal": {
                    "value": 1007
                },
                "jumlah_sembuh": {
                    "value": 32615
                },
                "jumlah_positif": {
                    "value": 36197
                },
                "jumlah_dirawat": {
                    "value": 2575
                },
                "jumlah_positif_kum": {
                    "value": 2527203
                },
                "jumlah_sembuh_kum": {
                    "value": 2084724
                },
                "jumlah_meninggal_kum": {
                    "value": 66464
                },
                "jumlah_dirawat_kum": {
                    "value": 376015
                }
            }
        ],
        "total": {
            "jumlah_positif": 2527203,
            "jumlah_dirawat": 376015,
            "jumlah_sembuh": 2084724,
            "jumlah_meninggal": 66464
        }
    }
}