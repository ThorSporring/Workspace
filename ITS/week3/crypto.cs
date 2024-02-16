using System;
using System.IO;
using System.Text;
using System.Security.Cryptography;

namespace Crypto_Aes
{
    public class Crypto
    {

        public static void Main(){
            
            
            var aes = Aes.Create();
            aes.KeySize = 128;
            aes.Key = new byte[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 };
            aes.IV = new byte[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 };
            
            var encryptor = aes.CreateEncryptor();
            var encrypted_msg = new byte[0];
            string myMessage = "Hello guys, it's Nicole";

            

            using (MemoryStream msEncrypt = new MemoryStream())
            {   
                using (CryptoStream csEncrypt = new CryptoStream(msEncrypt, encryptor, CryptoStreamMode.Write))
                {
                    using (StreamWriter swEncrypt = new StreamWriter(csEncrypt))
                    {
                        //Write all data to the stream.
                        swEncrypt.Write(myMessage);
                    }
                     encrypted_msg = msEncrypt.ToArray();
                }
            }

            var decryptor = aes.CreateDecryptor();
            var decryptedMessage = "";
            using (MemoryStream msDecrypt = new MemoryStream(encrypted_msg))
            {
                using (CryptoStream csDecrypt = new CryptoStream(msDecrypt, decryptor, CryptoStreamMode.Read))
                {
                    using (StreamReader swDecrypt = new StreamReader(csDecrypt))
                    {
                        decryptedMessage = swDecrypt.ReadToEnd();
                    }
                    
                }
            }


            Console.Write("Unencrypted message: " + myMessage + "\n");
            Console.Write("Encrypted message: ");
            Console.Write(Encoding.ASCII.GetString(encrypted_msg) + "\n");
            Console.Write("Dencrypted message: ");
            Console.Write(decryptedMessage + "\n");


        }
    }
}
