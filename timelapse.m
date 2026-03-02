% --- Settings ---
exposure_us = 1000;   % exposure time in microseconds
gain_dB     = 1.0;     % gain in dB
save_dir    = 'C:\Users\YourName\Documents\camera_output';  % change this
interval_s  = 60;      % seconds between frames

% --- Setup ---
if ~exist(save_dir, 'dir'), mkdir(save_dir); end

vid = videoinput('gige', 1, 'Mono8');
src = getselectedsource(vid);
src.ExposureTime = exposure_us;
src.Gain         = gain_dB;

fprintf('Acquiring every %d seconds. Press Ctrl+C to stop.\n', interval_s);

frame_num = 1;
while true
    frame    = getsnapshot(vid);
    filename = fullfile(save_dir, sprintf('image_%04d.png', frame_num));
    imwrite(frame, filename);
    fprintf('[%s] Saved %s\n', datestr(now,'HH:MM:SS'), filename);
    frame_num = frame_num + 1;
    pause(interval_s);
end