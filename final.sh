
python lcd_twoline.py "" "" 

python lcd_twoline.py "NFC PENDRIVE" ""
echo 
echo "NFC PENDRIVE"
echo "----------------------"
sleep 1.5

python lcd_twoline.py "Place your NFC" "Pendrive on Dock"

sudo explorenfc-wifi-connect


python lcd_twoline.py "" ""

echo ">>>DRIVE CONNECTED<<<"
python lcd_twoline.py "DRIVE CONNECTED" ""
sleep 1.5
python lcd_twoline.py "Opening Pendrive" ""

sleep 1.5
python lcd_twoline.py "You can now" "transfer data" 

nautilus smb://mylinkit.local/

echo ">>>DRIVE DISCONNECTED<<<"
python lcd_twoline.py "DRIVE           " "   DISCONNECTED"

sleep 2.5
python lcd_twoline.py "NFC PENDRIVE" ""

