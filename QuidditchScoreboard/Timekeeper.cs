using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using WebSocketSharp;
//usingebSocketSharp.Net;
using System.Threading;
//using System.Net.WebSockets;
using Newtonsoft.Json;
using System.Net;
using Newtonsoft.Json.Linq;

namespace QuidditchScoreboard
{
    public partial class Timekeeper : Form
    {
        public Timekeeper()
        {
            InitializeComponent();
        }


        private void Button_CloseTimekeeper_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void Button_TimekeeperConnect_Click(object sende, EventArgs b)
        {
            // Create a new instance of the WebSocket class.
            //
            // The WebSocket class inherits the System.IDisposable interface, so you can
            // use the using statement. And the WebSocket connection will be closed with
            // close status 1001 (going away) when the control leaves the using block.
            //
            // If you would like to connect to the server with the secure connection,
            // you should create a new instance with a wss scheme WebSocket URL.

            using (var nf = new Notifier())
            using (var ws = new WebSocket("wss://quidditch.me:443/ws"))
            //using (var ws = new WebSocket ("wss://echo.websocket.org"))
            //using (var ws = new WebSocket ("ws://localhost:4649/Echo"))
          
            {
                // Set the WebSocket events.

                ws.OnOpen += (sender, e) => ws.Send("{'auth:" + textBox_TimekeeperAuthent.Text +",public_id:" + textBox_TimekeeperID.Text +"}"); ;

                ws.OnMessage += (sender, e) =>
                    nf.Notify(
                      new NotificationMessage
                      {
                          Summary = "WebSocket Message",
                          Body = !e.IsPing ? e.Data : "Received a ping.",
                          Icon = "notification-message-im"
                      }
                    );



        ws.OnError += (sender, e) =>
                    nf.Notify(
                      new NotificationMessage
                      {
                          Summary = "WebSocket Error",
                          Body = e.Message,
                          Icon = "notification-message-im"
                      }
                    );

                ws.OnClose += (sender, e) =>
                    nf.Notify(
                      new NotificationMessage
                      {
                          Summary = String.Format("WebSocket Close ({0})", e.Code),
                          Body = e.Reason,
                          Icon = "notification-message-im"
                      }
                    );
#if DEBUG
                // To change the logging level.
                ws.Log.Level = LogLevel.Trace;

                // To change the wait time for the response to the Ping or Close.
                //ws.WaitTime = TimeSpan.FromSeconds (10);

                // To emit a WebSocket.OnMessage event when receives a ping.
                //ws.EmitOnPing = true;
#endif
                // To enable the Per-message Compression extension.
                //ws.Compression = CompressionMethod.Deflate;

                // To validate the server certificate.
                /*
                ws.SslConfiguration.ServerCertificateValidationCallback =
                  (sender, certificate, chain, sslPolicyErrors) => {
                    ws.Log.Debug (
                      String.Format (
                        "Certificate:\n- Issuer: {0}\n- Subject: {1}",
                        certificate.Issuer,
                        certificate.Subject
                      )
                    );
                    return true; // If the server certificate is valid.
                  };
                 */

                // To send the credentials for the HTTP Authentication (Basic/Digest).
                //ws.SetCredentials ("nobita", "password", false);

             

                // To send the cookies.
                //ws.SetCookie (new Cookie ("name", "nobita"));
                //ws.SetCookie (new Cookie ("roles", "\"idiot, gunfighter\""));

                // To enable the redirection.
                //ws.EnableRedirection = true;

                // Connect to the server.
                ws.Connect();

                // Connect to the server asynchronously.
                //ws.ConnectAsync ();

                Console.WriteLine("\nType 'exit' to exit.\n");
                byte[] data = new byte[4096];
                while (true)
                {
                     Thread.Sleep(1000);
                     Console.Write("> ");
                     var msg = Console.ReadLine();
                     if (msg == "exit")
                         break;
                   
                }
              

            }
           
        }
       
    }
}
