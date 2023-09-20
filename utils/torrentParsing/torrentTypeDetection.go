package main

import (
	"fmt"
	"net/url"
	"os"
	"regexp"
	"strings"
)

// Function to determine if item in array exists in string
func containsAny(title string, Elements []string) bool {
	for _, element := range Elements {
		if strings.Contains(title, element) {
			return true
		}
	}
	return false
}

// Determine if torrent is TV 
func isTv(title string) bool {
	// TV S01E01-S99E99 Match
	r, _ := regexp.Compile("s\\d\\de\\d\\d")

	if r.MatchString(title) {
		return true
	}

	// TV S01.COMPLETE - S99.COMPLETE
	r, _ = regexp.Compile("s\\d\\d.complete")
	if r.MatchString(title) {
		return true
	}

	TVElements := []string{"hdtv", "tgxdoc", "web.x264"}

	return containsAny(title, TVElements)
}

// Determine if torrent is Movie
func isMovie(title string) bool {
  // Match with quality, release group, other tags
	MovieElements := []string{"480p", "720p", "1080p", "1920x1080", "2160p",
		"hdcam", "sunscreen[tgx]", "telesync", "webrip", "amzn", "web-dl", "x264",
		"h264", "h265", "x265", "web.h264", "remux", "hevc", "mp4", "mkv",
		"hdrip", "dvdrip", "blu-ray", "camrip", "bluray"}

	return containsAny(title, MovieElements)
}

// Determine if torrent is Music 
func isMusic(title string) bool {
	MusicElements := []string{"music", "albums", "+releases", "mp3", "320kbps",
		"tiktok+trending", "192khz", "24bit", "pmedia", "flac", "songs",
		"buildboards", "bob marley"}

	return containsAny(title, MusicElements)
}

// Determine if torrent is Game
func isGame(title string) bool {
	GameElements := []string{"fitgirl", "console", "digital+deluxe",
		"deluxe.edition", "repack", "early access", "tenoke", "dlc"}

	return containsAny(title, GameElements)

}

func TorrentType(title string) string {
	if isTv(title) {
		return "TV"
	} else if isMovie(title) {
		return "Movie"
	} else if isMusic(title) {
		return "Music"
    // Only known tag for eBook
	} else if strings.Contains(title, "epub") {
		return "eBook"
	} else if isGame(title) {
		return "Game"
	}

	return "Unknown"
}

func main() {
	if len(os.Args) != 2 {
		fmt.Println("Usage: go run torrentTypeDetection.go <Magnet URL>")
		return
	}
	var magnet string = os.Args[1]

	magnetUrl, err := url.Parse(magnet)
	if err != nil {
		panic(err)
	}

	keys, _ := url.ParseQuery(magnetUrl.RawQuery)
	title := keys.Get("dn")

	fmt.Println(TorrentType(strings.ToLower(title)))
}
