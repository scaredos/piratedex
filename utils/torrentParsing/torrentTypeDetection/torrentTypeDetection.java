import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class torrentTypeDetection {
    private static Boolean containsAny(String magnet, String elements[]) {
        for (String s : elements) {
            if (magnet.contains(s)) {
                return true;
            }
        }
        return false;
    }

    private static Boolean isTV(String magnet) {
        Pattern pattern = Pattern.compile("s\\d\\de\\d\\d", Pattern.CASE_INSENSITIVE);
        Matcher matcher = pattern.matcher(magnet);
        if (matcher.find()) {
            return true;
        }
        pattern = Pattern.compile("s\\d\\d.complete", Pattern.CASE_INSENSITIVE);
        matcher = pattern.matcher(magnet);
        return matcher.find();
    }

    private static Boolean isMovie(String magnet) {
        String elements[] = { "480p", "720p", "1080p", "1920x1080", "2160p",
                "hdcam", "sunscreen[tgx]", "telesync", "webrip", "amzn", "web-dl", "x264",
                "h264", "h265", "x265", "web.h264", "remux", "hevc", "mp4", "mkv",
                "hdrip", "dvdrip", "blu-ray", "camrip", "bluray" };

        return containsAny(magnet, elements);
    }

    private static Boolean isMusic(String magnet) {
        String elements[] = { "music", "albums", "+releases", "mp3", "320kbps",
                "tiktok+trending", "192khz", "24bit", "pmedia", "flac", "songs",
                "buildboards", "bob marley" };

        return containsAny(magnet, elements);
    }

    private static Boolean isGame(String magnet) {
        String elements[] = { "fitgirl", "console", "digital+deluxe",
                "deluxe.edition", "repack", "early access", "tenoke", "dlc" };

        return containsAny(magnet, elements);
    }

    private static String torrentType(String magnet) {
        if (isTV(magnet)) {
            return "TV";
        } else if (isMovie(magnet)) {
            return "Movie";
        } else if (isMusic(magnet)) {
            return "Music";
        } else if (isGame(magnet)) {
            return "Game";
        } else if (magnet.contains("epub")) {
            return "eBook";
        }
        return "Unknown";
    }

    public static void main(String[] args) {
        String magnet = args[0].toLowerCase();
        System.out.println(torrentType(magnet));
    }
}
