URL=http://localhost:6543/api
H="Content-Type: application/json"

echo "===== MAHASISWA ====="
echo "--- GET all";    curl -s -w "  [%{http_code}]\n" $URL/mahasiswa
echo "--- GET 1";      curl -s -w "  [%{http_code}]\n" $URL/mahasiswa/1
echo "--- POST";       curl -s -w "  [%{http_code}]\n" -X POST $URL/mahasiswa -H "$H" -d '{"nim":"123140028","nama":"Eka Putri","jurusan":"Teknik Informatika"}'
echo "--- PUT 1";      curl -s -w "  [%{http_code}]\n" -X PUT $URL/mahasiswa/1 -H "$H" -d '{"alamat":"Lampung Selatan"}'
echo "--- DELETE 2";   curl -s -w "  [%{http_code}]\n" -X DELETE $URL/mahasiswa/2

echo "===== MATAKULIAH ====="
echo "--- GET all";    curl -s -w "  [%{http_code}]\n" $URL/matakuliah
echo "--- GET 1";      curl -s -w "  [%{http_code}]\n" $URL/matakuliah/1
echo "--- GET 99 (404)"; curl -s -w "  [%{http_code}]\n" $URL/matakuliah/99
echo "--- POST";       curl -s -w "  [%{http_code}]\n" -X POST $URL/matakuliah -H "$H" -d '{"kode_mk":"IF3028","nama_mk":"Pengembangan Aplikasi Web","sks":3,"semester":5}'
echo "--- POST tidak lengkap (400)"; curl -s -w "  [%{http_code}]\n" -X POST $URL/matakuliah -H "$H" -d '{"kode_mk":"IF9999"}'
echo "--- PUT 1";      curl -s -w "  [%{http_code}]\n" -X PUT $URL/matakuliah/1 -H "$H" -d '{"sks":4}'
echo "--- DELETE 3";   curl -s -w "  [%{http_code}]\n" -X DELETE $URL/matakuliah/3