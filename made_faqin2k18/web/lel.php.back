<?php
@chdir('/tmp/faqin');
if (isset($_GET['fck']) && strlen($_GET['fck']) <= 8) {
    @exec('echo -n '.base64_decode($_GET['fck']));
} else if (isset($_GET['reset'])) {
    @exec('/bin/rm -rf /tmp/faqin/*');
}
?>
