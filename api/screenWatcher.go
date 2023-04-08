package main

import (
	"bytes"
	"os/exec"
	"strings"

	"github.com/gofiber/fiber"
)

// getScreens returns a string array
// The returned array contains the output of "screen -ls" as a list, seperated
// by the newline character.
func getScreens() []string {
	cmd := exec.Command("/usr/bin/screen", "-ls")
	var out bytes.Buffer
	cmd.Stdout = &out
	err := cmd.Run()
	var x []string
	if err != nil {
		if strings.Contains(out.String(), "No sockets") {
			x = nil
		} else {
			x = strings.Split(out.String(), "\n")
		}
	}
	return x
}

func main() {
	app := fiber.New()

	app.Get("/api/screens", func(c *fiber.Ctx) {
		screens := getScreens()
		if len(screens) == 3 {
			c.JSON(&fiber.Map{
				"success": true,
				"screens": []string{},
			})
			return
		}
		screens = screens[:len(screens)-3]
		screens = screens[1:]
		c.JSON(&fiber.Map{
			"success": true,
			"screens": screens,
		})
		return
	})
  
  // Port 2052 so I am able to route these through Cloudflare and not expose server IPs
	app.Listen(2052)
}
